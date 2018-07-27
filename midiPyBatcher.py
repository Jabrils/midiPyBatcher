import os
import argparse
import mcf as backend

# standard argparse stuff
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='** = required')
parser.add_argument('-d', "--exe_dir", type=str,
    help='** you have to point to the directory to midicvs')
parser.add_argument('-sl', "--save_log", action='store_true',
    help='add the -sl flag to save a log of the process')
parser.add_argument('-bt', "--batch_text", action='store_true',
    help='add the -bt flag to batch all text files in Batch Texts converting them to .mid')
parser.add_argument('-bm', "--batch_midi", action='store_true',
    help='add the -bm flag to batch all midi files in Batch Midis converting them to .txt')
args = parser.parse_args()

thisDir = os.getcwd()

allFoldersNeeded = ['Batch Midis','Batch Txt', 'Converted to Midis', 'Converted to Txt']

# 
for i in range(len(allFoldersNeeded)):
    if not os.path.exists(allFoldersNeeded[i]):
        os.makedirs(allFoldersNeeded[i])

# 
if args.batch_text:
    backend.Batch(args,thisDir,allFoldersNeeded[1],allFoldersNeeded[2], "txt","mid","csvmidi")

# 
if args.batch_midi:
    backend.Batch(args,thisDir,allFoldersNeeded[0],allFoldersNeeded[3], "mid","txt","midicsv")

print("...& DONE!")
