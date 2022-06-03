#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    length = len(sys.argv)
    for i in range(1, length):
        sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
