import time
import random
def swap(x,i,j):
	x[i]=x[i]+x[j]
	x[j]=x[i]-x[j]
	x[i]=x[i]-x[j]
	return x
	
if __name__=='__main__':
	x=[random.randrange(0,1000,2) for i in range(0,1000)]
	max=len(x)
	print(max)
	start=time.time()
	for i in range(0,max-1):
		for j in range(0,max-i-1):
			if x[j]>x[j+1]:
				x=swap(x,j,j+1)
	end=time.time()
	print("time taken is"+str(end-start))
			