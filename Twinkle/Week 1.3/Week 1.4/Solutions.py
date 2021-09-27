#Problem 1a
n = int(input("Enter a positive number:  "))
sum = 0
while n <=0:
    print("Error! You must enter a positive number.  ")
    n = int(input())

while n>0:
    sum += n
    n -= 1

print(sum)


#Problem 1b
n = int(input("Enter a positive number:  "))
sum = 0
while n <=0:
    print("Error! You must enter a positive number.  ")
    n = int(input())

for i in range(n):
    sum += n
    n -= 1

print(sum)

#Problem 2
n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)
