from itertools import groupby

def compress_the_string(s):
    for k, g in groupby(s):
        print("({}, {})".format(len(list(g)), k), end=" ")

if __name__ == '__main__':
    s = input()
    compress_the_string(s)
