Run on the command line, in the same directory that the theme folder is located.

The `user-data-dir` directory is scrubbed when Chrome closes.

Assuming the following:

 - Memory forensics were not performed (did you shut the machine down?)
 - You believe a single pass with random data is sufficient to destroy file data
 - Information you want destroyed is contained in the Chrome user-data-dir (I believe this to be the case, but dont quote me)

Then on-disk browsing history, cookies, settings etc should be destroyed.

Filenames/metadata are not scrubbed, so at the time of writing the following artifacts may be trivially discoverable by forensics:

 - Chrome extensions that were being used
 - Rough duration of session (inferred from file sizes)
 - Probably others
