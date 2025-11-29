from collections import deque

def piling_up(blocks):
    d = deque(blocks)
    last = float('inf')
    
    while d:
        if d[0] >= d[-1]:
            curr = d.popleft()
        else:
            curr = d.pop()
            
        if curr > last:
            return "No"
        last = curr
        
    return "Yes"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))
        print(piling_up(blocks))
