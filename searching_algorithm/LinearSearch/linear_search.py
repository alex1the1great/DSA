numbers = [1, 3, 4, 7, 6, 8]
target_value = 4

for index, number in enumerate(numbers):
    if number == target_value:
        print(f'Index of {target_value} is: {index}')
        break
else:
    print(f'{target_value} not found.')
