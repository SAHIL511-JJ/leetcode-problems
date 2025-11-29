def no_idea(arr, A, B):
    happiness = 0
    for i in arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1
    return happiness

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    print(no_idea(arr, A, B))
