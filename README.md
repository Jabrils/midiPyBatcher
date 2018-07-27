# midiPyBatcher
put a bunch of .mid's in a directory, run this script to batch convert it into .txt's, or vice-versa using midicsv!

# How To Use
* download midicsv (http://www.fourmilab.ch/webtools/midicsv/#Download)
* download midiPyBatcher (this script)
* run your terminal of choice
* use python to run midiPyBatcher.py
* point to the midicsv director using the -d flag
* use -bm to convert midi files to text, -bt to convert text files to midi & -sl to save the log
* enjoy the automation

# Program Arguments: (** = required)
```
  -h, --help            ** = required
  -d EXE_DIR, --exe_dir EXE_DIR
                        ** you have to point to the directory to midicvs
                        (default: None)
  -sl, --save_log       logs the info (default: False)
  -bt, --batch_text     logs the info (default: False)
  -bm, --batch_midi     logs the info (default: False)
```