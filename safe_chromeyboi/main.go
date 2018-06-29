package main

import (
	"crypto/rand"
	"errors"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
)

const redDot = `data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==`

var (
	heuristicSiteIsolation bool
	userDataDir            string
)

func chromePath() (string, error) {
	switch runtime.GOOS {
	case "darwin":
		return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", nil
	}
	return "", errors.New("unknown platform: " + runtime.GOOS)
}

func initFlags() {
	flag.BoolVar(&heuristicSiteIsolation, "--unsafe-heuristic-site-isolation", false, "Does NOT enforce site isolation")
	flag.Parse()
}

func makeChromeInvocation() ([]string, error) {
	out := []string{"--no-first-run", "--disable-default-apps", "--no-default-browser-check", "--enforce-webrtc-ip-permission-check", "--prerender-from-omnibox=disabled"}
	if !heuristicSiteIsolation {
		out = append(out, "--site-per-process")
	}
	out = append(out, "--user-data-dir="+userDataDir)
  wd, err := os.Getwd()
  if err != nil {
    return nil, err
  }
  out = append(out, "--load-extension=" + filepath.Join(wd, "red_chrome_theme"))
	out = append(out, redDot)
	return out, nil
}

func cleanup() {
	if err := filepath.Walk(userDataDir, func(path string, info os.FileInfo, err error) error {
    if info.IsDir() {
      return nil
    }

		f, err := os.OpenFile(path, os.O_RDWR, 0755)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Failed to open %q for scrub: %v\n", path, err)
			return nil
		}
		defer f.Close()

		if _, err := f.Seek(0, 0); err != nil {
			fmt.Fprintf(os.Stderr, "Failed to seek in %q for scrub: %v\n", path, err)
			return nil
		}
    fmt.Printf("Scrubbing %q with %d random bytes.\n", path, info.Size())
		_, err = io.CopyN(f, rand.Reader, info.Size())
		return err
	}); err != nil {
		fmt.Fprintf(os.Stderr, "Scrub failed: %v\n", err)
	}

	if err := os.RemoveAll(userDataDir); err != nil {
		fmt.Fprintf(os.Stderr, "Failed to delete %q: %v\n", userDataDir, err)
	}
}

func main() {
	initFlags()

	crPath, err := chromePath()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Could not find path to Chrome: %v\n", err)
		os.Exit(1)
	}

	userDataDir, err = ioutil.TempDir("", "")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Could create user-data-dir temporary directory: %v\n", err)
		os.Exit(1)
	}
	defer cleanup()

	args, err := makeChromeInvocation()
	if err != nil {
		cleanup() // Necessary cuz defers do not run  if os.Exit is called.
		fmt.Fprintf(os.Stderr, "Could create chrome invocation: %v\n", err)
		os.Exit(1)
	}

	cmd := exec.Command(crPath, args...)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		fmt.Fprintf(os.Stderr, "Chrome exited with error: %v\n", err)
	}
}
