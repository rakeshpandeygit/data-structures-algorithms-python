max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max+1):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
