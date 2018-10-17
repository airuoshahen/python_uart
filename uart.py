#!/usr/bin/env python
# coding: utf-8

# In[14]:


from tkinter import *

def btnClick():
    plist = list(serial.tools.list_ports.comports())
    
    if len(plist) <= 0:
        print('The serial port can not find!')
        return
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName,115200,timeout=0.5)
        if serialFd.isOpen():
            print(serialFd.name,' is open!')
        else:
            print(serialFd.name,' is close!')
        serialFd.write('RESET\n'.encode())
        readBytes = serialFd.readline()
        readStr = bytes.decode(readBytes)
        print(readStr)
        serialFd.close()
        return

root = Tk(className="我的第一个窗口程序");

textLabel = Label(root,text = '提示显示',justify=LEFT,padx=100)
textLabel.pack(side = TOP)

btn = Button(root)
btn['text']='RESET'
btn['command'] = btnClick
btn.pack(side = BOTTOM)

mainloop()

