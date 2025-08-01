l=[10,20,30,40,50]
element=20

if element in l:
	l.remove(element)
	print(f"{element}removed successfully.")
else:
	print(f"{element}not found in the list.")
	
	print("updated list:",l)
