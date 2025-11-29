from datetime import datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.strptime(t1, fmt)
    d2 = datetime.strptime(t2, fmt)
    return str(int(abs((d1 - d2).total_seconds())))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))
