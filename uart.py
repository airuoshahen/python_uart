#!/usr/bin/env python
# coding: utf-8

# In[18]:


import serial
import serial.tools.list_ports

#下面5--18行的程序可以打开一个串口
plist = list(serial.tools.list_ports.comports())

if len(plist) <= 0:
    print('The Serial port can not find!')
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    print(serialName)
    serialFd = serial.Serial(serialName,115200,timeout=0.5)
    print('check which port was really used >',serialFd.name)
    if serialFd.isOpen():
        print(serialFd.name,' is open!')
    else:
        print(serialFd.name,' is close!')
#下面19--25行的程序是如何运用串口读取发送数据
n = serialFd.write('uart test!'.encode())
print(serialFd.portstr)
print(n)
readBytes = serialFd.read(n)
readStr = bytes.decode(readBytes)
print(readStr)
serialFd.close()

