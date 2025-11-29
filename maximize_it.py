from itertools import product

def maximize_it(lists, m):
    results = map(lambda x: sum(i**2 for i in x) % m, product(*lists))
    return max(results)

if __name__ == '__main__':
    k, m = map(int, input().split())
    lists = []
    for _ in range(k):
        lists.append(list(map(int, input().split()))[1:])
    print(maximize_it(lists, m))
