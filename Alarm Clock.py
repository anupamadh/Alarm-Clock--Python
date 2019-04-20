# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 15:27:42 2019

@author: Anupama Dhir
"""
import time
import winsound

def procedure():
   time.sleep(2.5)
   #winsound.Beep(37, 2000)
  # winsound.PlaySound('/c/users/Anupama Dhir/Documents/Anu/Python/Alarm Clock/SampleAudio_0.4mb.mp3', winsound.SND_FILENAME) 
   winsound.MessageBeep()

# measure process time
t0 = time.clock()
procedure()
print (time.clock(), "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")