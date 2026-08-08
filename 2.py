print("COUNT DOWN TIMER!")

def countdown(num):
    if num==0:
        print("TIMES UP!")
    
    print(num)

num=int(input("Enter a number"))
print(countdown(num))

def countup(num):
    if num>=10:
        print("Reached 10!")
    num=num+1

