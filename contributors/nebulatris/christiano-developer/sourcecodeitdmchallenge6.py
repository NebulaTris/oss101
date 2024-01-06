import random as rn
print("Guess the number!! in  3 guesses, abs int will be handled")
print("ranging from 0 to 100, endpoints included")
a = rn.randint(0,100)
count = 0
print(a)
def check(count):
    b = int(input())
    
    if b > 100:
        return "Out of bound READ!"
    if count > 2:
        print("booo")
    
    if a == b:
       print("Genius")
    elif b > a:
        print("Lower")
        check(count)
    else:
        print("Higher")
        check(count)
    count += 1
check(count)