sp = 35
st = 1
for x in range(0,17):
	for y in range(0,sp):
		print(" ",end="")
	for y in range(0,st):
		print("*",end="")	
	print()
	if x>=8:
		sp=sp+1
		st=st-2
	else:
		sp=sp-1
		st=st+2
