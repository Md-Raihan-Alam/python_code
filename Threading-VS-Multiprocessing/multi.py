from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

processes=[]
num_processes=os.cpu_count()
# create processes
for i in range(num_processes):
    # p=Process(target=square_numbers,args=(`enter arguments here`)) for arguemnts
    p=Process(target=square_numbers) # call of object or function that is executed by Process
    processes.append(p)

# start 
for p in processes:
    p.start()

if __name__ == '__square_numbers__':
    # freeze_support() here if program needs to be frozen
    square_numbers()  # execute this only when run directly, not when imported!

# join
for p in processes:
    p.join()

print('end main')