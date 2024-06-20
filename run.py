#coding=utf-8
import os, sys, platform
try:
    if sys.argv[1]=='update':
        os.system('rm -rf clone.so clone32.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('clone.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/clone.cpython-311.so?raw=true -o clone.so')
        os.system('chmod 777 clone.so')
        from clone import reg
        reg()
    else:
        from clone import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('clone32.so'):
        os.system('curl -L https://github.com/SHOOTER-MAKER/Juttbrand/blob/main/clone32.cpython-311.so?raw=true -o clone32.so')
        os.system('chmod 777 clone32.so')
        from clone32 import reg
        reg()
    else:
        from clone32 import reg
        reg()
else:
    print ('Your device is not supported ')
    exit()
