# Pyramid pattern using '*'
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

if __name__ == "__main__":
    try:
        rows = int(input("Enter the number of rows for the pyramid: "))
        print_pyramid(rows)
    except ValueError:
        print("Please enter a valid integer.")

