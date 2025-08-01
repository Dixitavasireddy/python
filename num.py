n=[24,23,25,65,84]
even=[]
odd=[]
for num in n:
	if num%2==0:
		even.append(num)
	else:
		odd.append(num)
		print("even numbers:",even)
		print("odd numbers:",odd)
