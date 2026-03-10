#  PRELAB – Awareness of Google Colab/VS Code and Implement a Python
#  Program to find a magic square of given dimension. 

def generate_magic_square(n):
    magic_square = [[0] * n for _ in range(n)]
    i, j = 0, n // 2

    for num in range(1, n * n + 1):
        magic_square[i][j] = num
        i -= 1
        j += 1

        if num % n == 0:
            i += 2
            j -= 1
        elif j == n:
            j -= n
        elif i < 0:
            i += n

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        print(" ".join(str(num) for num in row))

n = 3  
magic_square = generate_magic_square(n)
print_magic_square(magic_square)