A = int(input("Number 1: "))
B = int(input("Number 2: "))

if A <= B:
    for nums in range(A, B + 1):
        print(nums)
else:
    print("Error")