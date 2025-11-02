class yuva:
	def ram(self,a):
		for i in range(a):
			print( )	
			for j in range(i,a):
				print(" ",end=" ")
			for j in range(i+1):
				print("*",end=" ")
			for j in range(i):
				print("*",end=" ")
			
			
ob1=yuva()
ob1.ram(5)

class sub:
	def ran(self,a):
		for i in range(a):
			print()
			for j in range(i+1):
				print(" ",end=" ")
			for j in range(i,a):
				print("*",end=" ")
			for j in range(i,a-1):
				print("*",end=" ")
				
				
ob2=sub()
ob2.ran(5)