import pickle
def NS(s):
      ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    f=open("secret.dat","wb")
    pickle.dump(s,f)
    f.close()
    f=open("secret.dat","r")
    return f.read()
def SN(s):
    f=open("secret.dat","w")
    f.write(s)
    f.close()
    f=open("secret.dat","rb")
    c=pickle.load(f)
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

def jump(distanz, winkel=0):
    penup()
    right(winkel)
    forward(distanz)
    left(winkel)
    pendown()

def hand(laenge, spitze):
    fd(laenge*1.15)
    rt(90)
    fd(spitze/2.0)
    return c

    
