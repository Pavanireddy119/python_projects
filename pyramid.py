# Pyramid pattern using '*'
def print_pyramid():
    rows = int(input("Enter the number of rows: "))
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

if __name__ == "__main__":
    print_pyramid()
