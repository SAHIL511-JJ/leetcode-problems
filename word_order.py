from collections import OrderedDict

def word_order(words):
    od = OrderedDict()
    for word in words:
        od[word] = od.get(word, 0) + 1
    
    print(len(od))
    print(*od.values())

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    word_order(words)
//alright
