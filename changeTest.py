#! usr/bin/python3

import sys
from timeit import default_timer as timer
import resource

def get_change(n):
    D = (n - (n % 10)) / 10  # dimes
    if (n % 10) >= 5:   # if nickels
        N = 1   # 1 nickel
        P = (n % 10) - 5    # rest of the remainder pennies
    if (n % 10) < 5:    # if no nickels
        P = (n % 10)    # pennies
    return int(D + N + P)    # total num coins

def main():
    n = int(sys.stdin.readline())
    start = timer()
    print(get_change(n))
    end = timer()
    print(end - start)
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e06)

if __name__ == '__main__':
    main()
