#TAG1 倒计时函数-递归条件和基线条件

def countdown(i):
    print(i)
    countdown(i - 1)

countdown(3)

def countdown(i):
    print(i)
    if i == 0:
        return
    else:
        countdown(i - 1)

countdown(5)

#TAG2 greet函数-调用栈

def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye ...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")
def bye():
    print("OK, bye!")

greet("Rui TANG")

#TAG3 factorial函数—递归调用栈

def factorial(x):
    if (x == 1):
        return 1
    else:
        return(x * factorial(x-1))

factorial(5)