n=int(input("enter n value:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")            

# Pyramid pattern using '*'
def print_pyramid():
     rows = int(input("Enter the number of rows: "))
     for i in range(rows):
          print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

# Uncomment the following line to run the pyramid program
# print_pyramid()
