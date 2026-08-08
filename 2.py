print("COUNT DOWN TIMER!")

def countdown(num):
    if num==0:
        print("TIMES UP!")
        return
    print(num)
    return countdown(num-1)
    

num=int(input("Enter a number"))
countdown(num)

def countup(num):
    if num>=10:
        print("Reached 10!")
        return
    print(num)
    return countup(num+1)

countup(1)


def factorial(num):
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

n=int(input("Enter a number"))
print(f"Factorial of {n}: {factorial(n)}")


#Unsafe condition
#Stack overflow

def errorstack(n):
    print(n)

#It is dangerous hence not printing