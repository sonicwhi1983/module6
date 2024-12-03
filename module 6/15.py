import multiprocessing 

def now(secsonds): 
    from datetime import datetime 
    from time import sleep 
    sleep(secsonds) 
    print('wait', secsonds, 'seconds, time is', datetime.utcnow()) 

if __name__ == '__main__': 
    import random 
    for n in range(3): 
        seconds = random.random() 
        proc = multiprocessing.Process(target=now, args=(seconds,)) 
        proc.start() 
            