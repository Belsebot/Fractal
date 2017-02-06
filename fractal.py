from PIL import Image

data = ""

a=500
pile=[[0 for x in range(a)]for y in range(a)]

#piles
pile[250][250]=50000


loop=True
count=0

while loop:
	loop=False
	for x in range(a):
		for y in range(a):
			if pile[x][y] > 3:
				if pile[x][y] % 4 == 0:
					b=pile[x][y]/4
					pile[x][y]-=pile[x][y]
					if x<a-1:
						pile[x+1][y]+=b
					if x>0:
						pile[x-1][y]+=b
					if y<a-1:
						pile[x][y+1]+=b
					if y>0:
						pile[x][y-1]+=b

				else:
					pile[x][y]-=4
					if x<a-1:
						pile[x+1][y]+=1
					if x>0:
						pile[x-1][y]+=1
					if y<a-1:
						pile[x][y+1]+=1
					if y>0:
						pile[x][y-1]+=1
				loop=True
	count+=1


for x in range(a):
	for y in range(a):
		if pile[x][y]==3:
			data+=chr(255)+chr(0)+chr(0)
		if pile[x][y]==2:
			data+=chr(0)+chr(255)+chr(0)
		if pile[x][y]==1:
			data+=chr(0)+chr(0)+chr(255)
		if pile[x][y]==0:
			data+=chr(0)+chr(0)+chr(0)

im=Image.frombytes("RGB",(len(pile),len(pile[0])),data)
im.save("Fractal.png","PNG")
print "%d looppia loppu" % count

