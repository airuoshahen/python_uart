#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import operator
import serial
import serial.tools.list_ports
import _thread
import time
from tkinter import *

global openSerialList
global serialToTagNumList
global lastRecvStrecStrList

openSerialList = []
serialToTagNumList = []
lastRecvStrecStrList = []

def btnResetCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('RESET\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Reset failed!')
			else:
				print(openSerialList[i].portstr+' Reset success!')

def btnMpuonCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('MPUON\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Mpuon failed!')
			else:
				print(openSerialList[i].portstr+' Mpuon success!')
                
def btnMpuofCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('MPUOF\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Mpuof failed!')
			else:
				print(openSerialList[i].portstr+' Mpuof success!')
                
def btnSlotCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('SLOT\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Slot failed!')
			else:
				print(openSerialList[i].portstr+' Slot success!')
                
def btnSmagCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('SMAG\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Smag failed!')
			else:
				print(openSerialList[i].portstr+' Smag success!')
                
def btnSteponCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('STEPON\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Stepon failed!')
			else:
				print(openSerialList[i].portstr+' Stepon success!')
                
def btnStepofCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('STEPOF\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Stepof failed!')
			else:
				print(openSerialList[i].portstr+' Stepof success!')
                
def btnDisonCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('DISON\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Dison failed!')
			else:
				print(openSerialList[i].portstr+' Dison success!')
                
def btnDisofCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('DISOF\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Disof failed!')
			else:
				print(openSerialList[i].portstr+' Disof success!')

def btnMagonCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('MAGON\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Magon failed!')
			else:
				print(openSerialList[i].portstr+' Magon success!')
                
def btnMagofCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('MAGOF\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Magof failed!')
			else:
				print(openSerialList[i].portstr+' Magof success!')
                
def btnUwbonCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('UWBON\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Uwbon failed!')
			else:
				print(openSerialList[i].portstr+' Uwbon success!')
                
def btnUwbofCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
#			if serialToTagNumList[i] > 0 and serialToTagNumList[i] < 5:
			try:
				openSerialList[i].write('UWBOF\r\n'.encode())
			except:
				print(openSerialList[i].portstr+' Uwbof failed!')
			else:
				print(openSerialList[i].portstr+' Uwbof success!')
                
def btnCloseCallback():
    if len(openSerialList) <= 0:
        print('len <= 0')
        return
    else:
        for i in range(0,len(openSerialList)):
			try:
				openSerialList[i].close()
			except:
				print(openSerialList[i].portstr+' Close failed!')
			else:
				print(openSerialList[i].portstr+' Close success!')
					
def guiShow():
    root = Tk()

    root.title('HansonCom')

    root.geometry("700x550")

    btnReset = Button(text="RESET", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnReset['command'] = btnResetCallback

    btnReset.place(x=10, y=10, width=100, height=40)

    btnMpuon = Button(text="MPUON", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnMpuon['command'] = btnMpuonCallback

    btnMpuon.place(x=10, y=60, width=100, height=40)
    
    btnMpuof = Button(text="MPUOF", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnMpuof['command'] = btnMpuofCallback

    btnMpuof.place(x=10, y=110, width=100, height=40)
    
    btnSlot = Button(text="SLOT", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnSlot['command'] = btnSlotCallback

    btnSlot.place(x=10, y=160, width=100, height=40)
    
    btnSmag = Button(text="SMAG", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnSmag['command'] = btnSmagCallback

    btnSmag.place(x=10, y=210, width=100, height=40)
    
    btnStepon = Button(text="STEPON", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnStepon['command'] = btnSteponCallback

    btnStepon.place(x=10, y=260, width=100, height=40)
    
    btnStepof = Button(text="STEPOF", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnStepof['command'] = btnStepofCallback

    btnStepof.place(x=10, y=310, width=100, height=40)
    
    btnDison = Button(text="DISON", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnDison['command'] = btnDisonCallback

    btnDison.place(x=10, y=360, width=100, height=40)
    
    btnDisof = Button(text="DISOF", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnDisof['command'] = btnDisofCallback

    btnDisof.place(x=10, y=410, width=100, height=40)
    
    btnMagon = Button(text="MAGON", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnMagon['command'] = btnMagonCallback

    btnMagon.place(x=10, y=460, width=100, height=40)
    
    btnMagof = Button(text="MAGOF", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnMagof['command'] = btnMagofCallback

    btnMagof.place(x=10, y=510, width=100, height=40)
    
    btnUwbon = Button(text="UWBON", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnUwbon['command'] = btnUwbonCallback

    btnUwbon.place(x=120, y=10, width=100, height=40)
    
    btnUwbof = Button(text="UWBOF", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnUwbof['command'] = btnUwbofCallback

    btnUwbof.place(x=120, y=60, width=100, height=40)
	
    btnClose = Button(text="CLOSE", borderwidth="2", font=("微软雅黑", 15), background="white")

    btnClose['command'] = btnCloseCallback

    btnClose.place(x=120, y=110, width=100, height=40)

    root.mainloop()

def save_to_file(file_name,contents):
    try:
        fh = open(file_name,'r+')
        fh.seek(0,2)
        fh.write(contents)
        fh.close()
    except:
        fh = open(file_name,'w')
        fh.write(contents)
        fh.close()
        

def comHandle():
    plist = list(serial.tools.list_ports.comports())

    if len(plist) <= 0:
        print('The Serial port can not find!')
    else:
        for i in range(0,len(plist)):
            plist_0 = list(plist[i])
            serialName = plist_0[0]
            print(serialName)
            try:
                serialFd = serial.Serial(serialName,115200,timeout=0.02)
                print('check which port was really used >',serialFd.name)
                if serialFd.isOpen():
					print(serialFd.name,' is open!')
					serialFd.WriteTimeout = 1
					openSerialList.append(serialFd)
					serialToTagNumList.append(5)
					lastRecvStrecStrList.append(['a'])
                else:
                    print(serialFd.name,' is close!')
            except:
                print(serialName,' open failed!')
    print(serialToTagNumList)
    print(openSerialList)
    time.sleep(10)
    #下面19--25行的程序是如何运用串口读取发送数据
    while True:
		if len(openSerialList)==0:
			print('no open serial!')
			break
		for i in range(0,len(openSerialList)):
			readBytes = openSerialList[i].readline()
			try:
				readStr = bytes.decode(readBytes)
			except:
				print(openSerialList[i].portstr,readBytes)
			else:
				if len(readStr) != 0:
					lastRecvStr = ','.join(lastRecvStrecStrList[i])
					if operator.ne(lastRecvStr,readStr):
						print(lastRecvStr,'is last')
						lastRecvStrecStrList.insert(i,readStr.split(','))
						lastRecvStrecStrList.pop(i+1)
						print(readStr,'is new')
						if 'slot' in readStr:
							serialToTagNumList.insert(i,int(readStr[-3],base=10))
							serialToTagNumList.pop(i+1)
							fileName = 'tag'+readStr[-3]+'.txt'
							print('fileName is '+fileName)
							save_to_file(fileName,'tag'+readStr[-3]+' save file test!\n')
						else:
							if serialToTagNumList[i] == 1:
								save_to_file('tag1.txt',readStr)
							elif serialToTagNumList[i] == 2:
								save_to_file('tag2.txt',readStr)
							elif serialToTagNumList[i] == 3:
								save_to_file('tag3.txt',readStr)
							elif serialToTagNumList[i] == 4:
								save_to_file('tag4.txt',readStr)
							else:
								print(openSerialList[i].portstr,'not get tag num!')
					else:
						print(openSerialList[i].portstr,'recv same str!')
					print(openSerialList[i].portstr,'recv',readStr)
#				else:
#					print(openSerialList[i].portstr,'recv nothing!')
#		print(serialToTagNumList)
    
        
if __name__ == '__main__':
    try:
        _thread.start_new_thread(comHandle,())
        _thread.start_new_thread(guiShow,())
    except:
        print('Error:无法启动线程!')
    
    while True:
		pass
