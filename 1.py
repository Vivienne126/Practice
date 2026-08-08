#FOR USER TO GIVE ELEMENTS IN LIST TO INPUT

n=int(input("Enter how many numbers?"))
l1=[]

for i in range(n):
    elements=int(input("Enter a number"))
    l1.append(elements)

print(l1)