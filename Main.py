"""
Title : MultiThreading Scheduling.
Created on Thu Apr  4 20:08:25 2019
@author: Uchiha Madara
"""
from threading import Thread
import threading
from graffiti import *
import time
#Required global variables.
lock = threading.Lock()


#Class for different threads.
class NThread (Thread): #Class for SJF and FCFS.
    name = ""
    bt = 0
    tat = 0
    wt = 0
    p = 0
    def __init__(self, name,bt, p = 0):
        self.name = name
        self.bt = bt
        self.p = p
    def run(self):
        for i in range(1,self.bt+1):
            print('Thread',self.name,'burst number :',i)
            time.sleep(0.25)




#User input for different threads.
def input_NThread():
    Nlist = []
    n = int(input('Enter the number of threads :> '))
    for i in range(n):
        name = input('Enter Thread\'s name :> ')
        bt = int(input('Enter Thread Burst Time :> '))
        N = NThread(name,bt)
        Nlist.append(N)
    return Nlist

#User input for priority thread:
def input_NThread2():
	Nlist = []
	n = int(input('Enter the number of threads :> '))
	for i in range(n):
		name = input('Enter Thread\'s name :>  ')
		bt = int(input('Enter Thread Burst Time :>  '))
		p = int(input('Enter priortiy :> '))
		N = NThread(name,bt,p)
		Nlist.append(N)
	return Nlist


#FCFS Threading
def FCFS():
    Nlist = input_NThread()
    avg_wt = 0
    avg_tat = 0
    for obj in Nlist:
        lock.acquire()
        obj.run()
        lock.release()
        
    Nlist[0].tat = Nlist[0].bt
    Nlist[0].wt = 0
    avg_tat+= Nlist[0].tat
    for i in range(1,len(Nlist)):
        Nlist[i].wt = Nlist[i-1].wt + Nlist[i-1].bt
        Nlist[i].tat = Nlist[i].wt + Nlist[i].bt
        avg_wt += Nlist[i].wt
        avg_tat += Nlist[i].tat
    avg_wt/=len(Nlist)
    avg_tat/=len(Nlist)
    print("Average Waiting Time :",avg_wt)
    print("Average Turn Around Time:",avg_tat)
    time.sleep(0.5)
    
    
        

def SJF():
    Nlist = input_NThread()
    Nlist.sort(key = lambda x: x.bt)
    avg_wt = 0
    avg_tat = 0
    for obj in Nlist:
        lock.acquire()
        obj.run()
        lock.release()
        Nlist[0].tat = Nlist[0].bt
    Nlist[0].wt = 0
    avg_tat+= Nlist[0].tat
    for i in range(1,len(Nlist)):
        Nlist[i].wt = Nlist[i-1].wt + Nlist[i-1].bt
        Nlist[i].tat = Nlist[i].wt + Nlist[i].bt
        avg_wt += Nlist[i].wt
        avg_tat += Nlist[i].tat
    avg_wt/=len(Nlist)
    avg_tat/=len(Nlist)
    print("Average Waiting Time :",avg_wt)
    print("Average Turn Around Time:",avg_tat)
    time.sleep(0.5)
    
    
#Priority Threading
def Priority():
	Nlist = input_NThread2()
	Nlist.sort(key = lambda x: x.p)
	avg_wt = 0
	avg_tat = 0
	for obj in Nlist:
		lock.acquire()
		obj.run()
		lock.release()
	Nlist[0].wt=0
	Nlist[0].tat = Nlist[0].bt
	avg_tat += Nlist[0].tat
	for i in range(1,len(Nlist)):
		Nlist[i].wt = Nlist[i-1].wt + Nlist[i-1].bt
		Nlist[i].tat = Nlist[i].wt + Nlist[i].bt
		avg_wt += Nlist[i].wt
		avg_tat += Nlist[i].tat
	avg_wt /= len(Nlist)
	avg_tat /= len(Nlist)
	print("Average Waiting Time : ",avg_wt)
	print("Average Turn Around Time: ",avg_tat)
	time.sleep(0.5)

    

        
opt = 0

while (opt!=6):
    
    print(Title)
    load_bar()

    time.sleep(0.05)
    print('\n')
    print(Menu)
    opt = int(input('Enter your Choice :> '))
    if(opt == 1):
      FCFS()
    elif(opt == 2):
      SJF()
    
    elif(opt == 3):
      Priority()
    
    elif (opt == 4):
        #Round Robin
        break
    elif(opt == 5):
        Credits_display()
    elif(opt == 6):
        break
    else:
        print('Incorrect option detected! Please try again!')
