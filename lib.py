##jryzkns 2017

from Tkinter import *
import psychopy.visual
import psychopy.event
import math
import random
import time

def getID():
	'''null->str'''
	##	gets Participant from the user by drawing a small window,
	##	this function will return whatever was put into the text
	##	field.

	##	Sample usage:
	##	PID = getID()
	##	datafile = open(PID,"w")
	
	def exit():
		'''null->null'''
		prompt.destroy()

	prompt = Tk()

	var = StringVar()
	label = Label( prompt, textvariable=var )
	var.set("Please input subject Number:")

	n = StringVar()
	data = Entry( prompt, textvariable = n)

	OK = Button(prompt, text ="OK", command = exit)

	label.pack()
	data.pack()
	OK.pack()

	prompt.mainloop()

	s = n.get()

	return s

def ringCoord(ringrad, n, i):
	'''int,int,int -> null'''
	##	takes the input values and calculates where a stimuli
	##	would be on a ring of radius ringrad and of position i
	##	if there were ttl circles evenly sitting on the ring
	return [ringrad * math.cos(2 * math.pi / n * i),ringrad * math.sin(2 * math.pi / n * i)]

def drawObjs(obj,ringrad, n):
	'''p.v.Stim,int,int'''
	##	uses the ringCoord function and draws out the stimuli
	##	on a ring
	for i in range(n):
		obj.pos = ringCoord(ringrad,n,i)
		obj.draw()


def setLine(line, setsize, setori, setpos):
	'''p.v.line,int,bool,int,ls[2]->null'''
	##	takes in an array of values to modify and draw out a
	##	line on the designated place. Useful to save resources
	##	by only declaring one line and using this to draw it
	##	whereever you want it to go
	line.size 	= setsize
	line.pos 	= pos
	line.ori 	= ori
	
	line.draw()

def randbool():
	'''null->bool'''
	##	literally flips a coin, picks an integer from 0 to 100
	##	if it is even, it returns True
	return ((random.randint(0,100) % 2) == 0)

def getAccuracy(target, inputls):
	'''str,ls->bool'''
	##	target is a list or a string, inputls is a list or string
	##	if elements of target is inside inputls, then it returns
	##	true. Useful in that if you have a set of keys that are
	##	what you want the subject to press, and you get their input
	##	data, you can simply use this to validate the accuracy

	accuracy = False	
	if (type(inputls) != NoneType):
		accuracy = target in inputls
	return accuracy


def autoscale(winsize,imgsize,screenscale):
	'''ls[2],ls[2],float->ls[2]'''
	##	automatically scales image size to fit in window, screenscale
	##	should be less than 1, the caller is responsible for giving
	##	the correct value. This function should be called right after
	##	the image object is declared.

	##	example usage(if the window is called main):
	##	img = p.v.ImageStim(...)
	##	img.size = autoscale(main.size,img.size,n)

	##	looks for the longest side for
	##	both the window and the image
	longerimgside = imgsize[0]
	correswinside = winsize[0]
	if (longerimgside < imgsize[1]):
		longerimgside = imgsize[1]
		correswinside = winsize[1]

	scaledsize = screenscale * correswinside

	scalefactor = scaledsize / longerimgside

	for i in range(len(imgsize)):
		imgsize[i] *= scalefactor

	return imgsize

'''LIST OF OBJECTS THAT SHOULD BE INCLUDED IN ALL PROJECTS'''

#main = psychopy.visual.Window(
#        units   = "pix",
#        fullscr = True,
#        color   = "#000000"
#)

#fcross = psychopy.visual.TextStim(
#	##	remember to call drawing this at the start of each drawloop
#	win	= main,
#	pos	= [0,1],	##slight offset to centre the cross
#	text	= "+",
#	color	= '#FFFFFF'
#)

