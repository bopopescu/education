from datetime import datetime
import random
import time

odds = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

#последовательный вывод с каждой строки
#for i in "123":

#повторение количество раз
for i in range(3):
    right_this_minute =datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems is litle odd.")
    else: 
        print("Not an odd minute")
    wait_time = random.randint(1,10)
    time.sleep(wait_time)