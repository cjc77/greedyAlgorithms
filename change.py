# Uses python3
import sys

def get_change(n):
    D = (n - (n % 10)) / 10  # dimes
    if (n % 10) >= 5:   # if nickels
        N = 1   # 1 nickel
        P = (n % 10) - 5    # rest of the remainder pennies
    if (n % 10) < 5:    # if no nickels
        P = (n % 10)    # pennies
    return int(D + N + P)    # total num coins    return n

def main():
    n = int(sys.stdin.readline())
    print(get_change(n))

if __name__ == '__main__':
    main()
