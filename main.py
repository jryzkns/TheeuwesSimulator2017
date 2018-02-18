#!/usr/bin/python

##jryzkns 2017

## ori: [45*0i, 45*i, 45*2i, 45*3i]

from lib import *

global n
n = 11

global ringrad
ringrad = 130

global trials
trials = 20


subject = getID()
f = open(subject,"w")
f.write("trial,RT,Accuracy\n")

main = psychopy.visual.Window(
	##size 	= [400,400],
	units 	= "pix",
	fullscr = True,##False,
	color 	= "#000000"
)

diamond = psychopy.visual.Polygon(
	win	= main,
	size	= 40*math.sqrt(2)*0.8,
	edges	= 4,
	lineColor= '#00FF00'
)

circ = psychopy.visual.Circle(
	win	= main,
	radius	= 20,
	edges	= 32,
	lineColor= '#00FF00'
)

line = psychopy.visual.Line(
	win	= main,
	size	= 15,
	pos	= [0,0],
	lineColor= '#FFFFFF',
	ori	= 0,
	lineWidth= 3
)

fcross = psychopy.visual.TextStim(
	win	= main,
	pos	= [0,1],	##slight offset to centre the cross
	text	= "+",
	color	= '#FFFFFF'
)

text = psychopy.visual.TextStim(
	win	= main,
	text	= "",
	color	= '#CCFFCC'
)


##	TOP	##

##text.text = "Welcome to this random study\nplease input subject number"
##text.draw()
##main.flip()

##subject = str(raw_input("Please input the subject number:"))+".csv"

text.text = "key left when the line is to the left\nkey right when the line is to the right\nkey up when the line is vertical\nkey space when the line is horizontal"
text.draw()
main.flip()

time.sleep(5)

text.text = "When you are ready, \npress any key to begin"
text.draw()
main.flip()
psychopy.event.waitKeys()


for j in range (trials):

	fcross.draw()

	temp = random.sample(range(n), 2)
	shapeOdd = temp[0]
	colorOdd = temp[1]
	targetoriout = 0	#will fetch the target orientation in the draw loop below

	##draw loop
	for i in range(n):
		circ.pos = ringCoord(ringrad, n, i)
		line.pos = ringCoord(ringrad, n, i)
		targetori = random.randint(0,3)
		line.ori = 45 * targetori
	
		if (i == colorOdd):
			circ.lineColor = "#FF0000"
			circ.draw()
			circ.lineColor = "#00FF00"
		elif (i == shapeOdd):
			diamond.pos = ringCoord(ringrad, n, i)
			diamond.draw()
			targetoriout = targetori
		else:
			circ.draw()
		line.draw()

	##calculates the correct key
	key = ""

	##if only we have switch statements lol
	if (targetoriout == 0):
		key = 'right'
	elif (targetoriout == 1):
		key = 'space'
	elif (targetoriout == 2):
		key = 'left'
	else:	##targetoriout == 3
		key = 'up'

	##trial starts
	main.flip()		##draws
	start = time.time()

##	keylist = psychopy.event.getKeys()	##we assume that the user only inputs one key
	keylist = psychopy.event.waitKeys(maxWait = 1.5)

##	print keylist

##	psychopy.event.waitKeys(maxWait = 2)	##this nullifies input xd

	end = 1000 * (time.time() - start)	##in milliseconds

	accuracy = getAccuracy(key,keylist)

#	##Trace Printing	
#	if accuracy:
#		print "correct!"
#	else:
#		print "wrong!"

	##write to file here
	info = str(j) + ',' + str(end) + ',' + str(accuracy) + '\n'
	f.write(info)

	time.sleep(0.5)	##wait time till next trial



text.text = "Thank you for participating\npress any key to exit"
text.draw()

main.flip()

psychopy.event.waitKeys()

f.close()
main.close()
