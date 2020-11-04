##import time
##def first():
##    print('First')
##    time.sleep(2)
##    return 1
##def second():
##    n = first()
##    print('Done')
##    n = n + 1
##    time.sleep(1)
##    print(n)
##
##while True:
##    second()

import os, time

def child(pipeout):
    while 1:
        print('Child')
        a = 1
        time.sleep(4)
        os.write(pipeout, a.to_bytes(2, 'big'))

def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        child(pipeout)
    else:
        while 1:
            num = os.read(pipein, 32)
            num = int.from_bytes(num, 'big')
            num = num + 1
            print(num)
            time.sleep(2)

parent()
        
