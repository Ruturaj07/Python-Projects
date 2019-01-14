# for i in range(1,10):
# 		for j in range(i):
# 			print("*", end=" ")
# 		print(end="\n")


# for i in range(1,10):
# 	if i%2 !=0:
# 		for j in range(i):
# 			print("*", end=" ")
# 		print(end="\n")

# num = 1
# while num < 11:
	
# 	print("*" * num)
# 	num += 2

n = input("Enter no. of rows : ")
n = int(n)
k = 2*n - 2

for i in range(1,n+1):
		for j in range(1,k+1):
			print(end=" ")
			k = k-2
		for j in range(i):
			print("*", end=" ")
		print(end="\n")

