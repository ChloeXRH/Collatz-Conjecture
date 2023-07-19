# this is the Collatz Conjecture: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1! 

firstTrue = True
secondTrue = True
def evenchecker(number):
    return number % 2 == 0

while firstTrue:
    try:
        num = int(input("Enter a number: " ))
        firstTrue = False
        break
    except:
        print("please use a number")

    
while secondTrue:    
    if evenchecker(num):
        num = num // 2
        print(num)
    else:
        num = num * 3 + 1
        print(num)
    
    if num == 1:
        secondTrue = False
        break