package main

import (
	"encoding/binary"
	"math"
	"os"
)

// go run main.go | aplay -f S16_LE -r 8000

var (
	bitsPerSample    int     = 16
	samplesPerSecond uint32  = 8000
	duration         int     = 2
	numberOfSamples  uint32  = samplesPerSecond * uint32(duration) // This is the length of the sound file in seconds
	frequency        float64 = 200
	volume           uint32  = 10000
	volumedB         float64 = 20 * math.Log10(float64(volume)/32767)
	phase            float64
	waveform         []uint16 = make([]uint16, numberOfSamples)
)

func main() {
	var temp []byte = make([]byte, 2)

	var frequencyRadiansPerSample = frequency * 2 * math.Pi / float64(samplesPerSecond)
	for sample := uint32(0); sample < numberOfSamples; sample++ {
		phase += frequencyRadiansPerSample
		sampleValue := float64(volume) * math.Sin(phase)
		waveform[sample] = uint16(sampleValue)
		binary.LittleEndian.PutUint16(temp, uint16(sampleValue))
		os.Stdout.Write(temp)
	}
}
