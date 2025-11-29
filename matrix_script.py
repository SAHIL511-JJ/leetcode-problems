import re

def matrix_script(matrix, n, m):
    decoded = ""
    for j in range(m):
        for i in range(n):
            decoded += matrix[i][j]
            
    print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', decoded))

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(input())
    matrix_script(matrix, n, m)
