from PIL import Image

data = ""

a=500							#picture size 500x500 pixel
pile=[[0 for x in range(a)]for y in range(a)]		#2d array

#piles
pile[250][250]=50000					#puts 50000 pile in center of the screen

loop=True						#set loop true
count=0							#counter set to zero

while loop:						#loop 
	loop=False					#set loop false if picture is ready then loop will stops
	for x in range(a):				
		for y in range(a):
			if pile[x][y] > 3:				#if there is pile which is bigger than 3
				if pile[x][y] % 4 == 0:			#check if pile can be divided by 4
					b=pile[x][y]/4			#divide pile size by 4
					pile[x][y]-=pile[x][y]		#and remove points from current pixel
					if x<a-1:			#check border
						pile[x+1][y]+=b		#distribute points to adjanced pixel
					if x>0:				#check border 
						pile[x-1][y]+=b		#distribute points to adjanced pixel
					if y<a-1:			#check border
						pile[x][y+1]+=b		#distribute points to adjanced pixel
					if y>0:				#check border
						pile[x][y-1]+=b		#distribute points to adjanced pixel

				else:					#if point is not divible by 4
					pile[x][y]-=4			#minus 4 from pile
					if x<a-1:			#and same as above but only adding 1 point to
						pile[x+1][y]+=1		#adjanced pixel
					if x>0:
						pile[x-1][y]+=1
					if y<a-1:
						pile[x][y+1]+=1
					if y>0:
						pile[x][y-1]+=1
				loop=True				#set loop to true if points have been tranfered
	count+=1							#add counter


for x in range(a):							#picture making
	for y in range(a):
		if pile[x][y]==3:					#if pixel value is 3
			data+=chr(255)+chr(0)+chr(0)			#then put pixel color to red
		if pile[x][y]==2:					#if pixel value is 2
			data+=chr(0)+chr(255)+chr(0)			#then put pixel color to green
		if pile[x][y]==1:					#if pixel value is 1
			data+=chr(0)+chr(0)+chr(255)			#then put pixel color to blue
		if pile[x][y]==0:					#if pixel value is 0
			data+=chr(0)+chr(0)+chr(0)			#then put pixel color to black

im=Image.frombytes("RGB",(len(pile),len(pile[0])),data)			#create image
im.save("Fractal.png","PNG")						#save image
print "%d loops end" % count					#show how many loops had to make

