import sys

def print_pyramid(n):
    """ Функция для печати пирамиды из символов '*' """
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python pyramid.py <количество уровней>")
    else:
        levels = int(sys.argv[1])
        print_pyramid(levels)
