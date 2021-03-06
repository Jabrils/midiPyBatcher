import os
import subprocess

# 
def Batch(args,thisDir,_batchDir, _outDir, _exe):
    _files = os.listdir(_batchDir)
    _filesChecked = []

    if _exe == 'midicsv':
        _from = 'mid'
        _to = args.ext
    else:
        _from = args.ext
        _to = 'mid'

    for c in _files:
        if _from in c:
            _filesChecked.append(c)
    
    print('checking the {} directory for batching!'.format(_batchDir))
    print("{} .{} files found!".format(len(_filesChecked),_from))

    # 
    if args.save_log:
        if not os.path.exists('Info Log'):
            os.makedirs('Info Log')

        # 
        for m in _filesChecked:
            os.chdir(thisDir)
            outfd = open("{}/{}.{}".format(_outDir,m.split('.')[0],_to),"w+")
            errfd = open("{}/{}.{}".format("Info Log",m,_to),"w+")
        
            print('\nconverting "{}" from .{} to .{}'.format(m,_from,_to))
        
            os.chdir('midicsv-1.1')
            subprocess.call([_exe,'-v',thisDir+"/"+_batchDir+"/"+m],stdout=outfd, stderr=errfd)
            outfd.close()
            errfd.close()
    else:
        for m in _filesChecked:
            os.chdir(thisDir)
            outfd = open("{}/{}.{}".format(_outDir,m.split('.')[0],_to),"w+")
    
            print('\nconverting "{}" from .{} to .{}'.format(m,_from,_to))

            os.chdir('midicsv-1.1')
            subprocess.call([_exe,'-v',thisDir+"/"+_batchDir+"/"+m],stdout=outfd)
            outfd.close()