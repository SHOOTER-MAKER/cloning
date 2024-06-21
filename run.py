#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf clone*')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('clone'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/clone?raw=true -o clone')
        os.system('chmod 777 clone')
        os.system('./clone')
    else:
        os.system('./clone')
elif bit == '32bit':
    if not os.path.isfile('clone32'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/clone32?raw=true -o clone32')
        os.system('chmod 777 clone32')
        os.system('./clone32')
    else:
        os.system('./clone32')
else:
    print ('Your device is not supported ')
    exit()
