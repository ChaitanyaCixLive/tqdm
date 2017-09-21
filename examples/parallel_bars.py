from __future__ import print_function
from time import sleep
from tqdm import tqdm
from multiprocessing import Pool, freeze_support, Lock


def progresser(n):
    interval = 0.001 / (n + 2)
    total = 5000
    text = "#{}, est. {:<04.2}s".format(n, interval * total)
    for _ in tqdm(range(total), desc=text, position=n):
        sleep(interval)


if __name__ == '__main__':
    freeze_support()  # for Windows support
    L = list(range(9))
    p = Pool(len(L))
    p.map(progresser, L)
    print("\n" * (len(L) - 1), end='')

    # alternatively, override default internal lock with our own
    p = Pool(len(L),
             initializer=tqdm.set_lock,
             initargs=(Lock(),))
    p.map(progresser, L)
    print("\n" * (len(L) - 1), end='')
