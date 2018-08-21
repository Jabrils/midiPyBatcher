# midiPyBatcher
put a bunch of .mid's in a directory, run this script to batch convert it into .txt's, or vice-versa using midicsv!

# How To Use
* download midiPyBatcher (this script)
* run your terminal of choice
* use python to run midiPyBatcher.py
* place whatever midi files you want to convert to text in Batch CSV, place whatever text files you want to convert to midi in Batch Midi
* use -bm to convert midi files to text, -bt to convert text files to midi, define -e if you are using something other than .csv & -sl to save the log
* enjoy the automation!

# Program Arguments: (** = required)
```
  -h, --help         ** = required
  -sl, --save_log    add the -sl flag to save a log of the process (default:
                     False)
  -bt, --batch_text  add the -bt flag to batch all text files in Batch Texts
                     converting them to .mid (default: False)
  -bm, --batch_midi  add the -bm flag to batch all midi files in Batch Midis
                     converting them to .csv (default: False)
  -e EXT, --ext EXT  add the -e flag to specify what extension you want to
                     read or write the midi file to (default: csv)
```