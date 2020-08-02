# Regan Willis 2020

import multiprocessing as mp
import time


def my_function(queue):
    data = queue.get()

    # loop through queue until flag is received
    while data:
        print(f'data received: {data}')
        data = queue.get()


if __name__ == "__main__":

    # create queue, start process
    queue = mp.Queue()
    process = mp.Process(target=my_function, args=(queue,))
    process.start()

    # loop through data
    for data in range(1, 31):

        # simulate data search taking some time
        time.sleep(0.25)

        # send qualifying data through the queue
        if data % 3 == 0:
            print('...sending data')
            queue.put(data)

    # send flag to stop process
    queue.put(False)
