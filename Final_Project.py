import time
def countdown(t):
    while t>0:
        print(t)
        t = t-1
        time.sleep(1)
    print("Always Be Happy \U0001F642") 
    
print("how many second to countdown? enter an integer.")
seconds=input()
while not seconds.isdigit():
    print("Thats wasn't an integer number! please enter an integer")
    seconds=input()
seconds = int(seconds)
countdown(seconds)
