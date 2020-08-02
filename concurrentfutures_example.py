# Regan Willis 2020

from time import sleep
from concurrent.futures import ProcessPoolExecutor


def my_function(data):

    # simulate computation on data
    if data == 9:
        sleep(4)
    else:
        sleep(1)

    print(f'data received: {data}')


if __name__ == "__main__":

    # create process pool
    executor = ProcessPoolExecutor()

    # loop through data
    for data in range(1, 31):

        # send qualifying data to the pool
        if data % 3 == 0:
            print('...sending data')
            executor.submit(my_function, data)