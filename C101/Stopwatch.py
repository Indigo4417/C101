import time


seconds = int(input('Enter the number of seconds: '))

def timer(seconds):
    while seconds > 0:
        min = int(seconds/60)
        sec = int(seconds%60)
        timer = f'{min}:{sec}'
        #print(timer, end='\r')
        print(timer)
        time.sleep(1)
        seconds -= 1
    print("Time's Up!")
    
timer(seconds)
