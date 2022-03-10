odd_number = [1, 3, 5, 7, 9]
even_number = []

for i in range(9):
    if i not in odd_number:
        even_number.append(i)

print(even_number)
