from itertools import combinations

def iterables_and_iterators(n, letters, k):
    indices = [i for i, x in enumerate(letters) if x == 'a']
    total_combinations = list(combinations(range(n), k))
    favorable = 0
    
    for comb in total_combinations:
        if any(i in indices for i in comb):
            favorable += 1
            
    return favorable / len(total_combinations)

if __name__ == '__main__':
    n = int(input())
    letters = input().split()
    k = int(input())
    print(iterables_and_iterators(n, letters, k))
