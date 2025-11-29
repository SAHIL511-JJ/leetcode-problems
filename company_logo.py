from collections import Counter

def company_logo(s):
    c = Counter(sorted(s))
    for k, v in c.most_common(3):
        print(k, v)

if __name__ == '__main__':
    s = input()
    company_logo(s)
