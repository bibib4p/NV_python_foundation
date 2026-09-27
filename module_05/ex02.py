# Statistics - Calculating a list of numbers with own total, number of, average, max, min functions

def main():
    numbers = [-43, 91, 91, 14, 0, 130]

    print(f"Total: {total(numbers)}")
    print(f"Number of : {number_of(numbers)}")
    print(f"Average : {average(numbers)}")
    print(f"Maximum : {maximum(numbers)}")
    print(f"Minimum : {minimum(numbers)}")

def total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def number_of(numbers):
    count = 0
    for number in numbers:
        count += 1
    return count

def average(numbers):
    return round(total(numbers) / number_of(numbers), 3)

def maximum(numbers):
    max_num = numbers[0]
    for i in range(number_of(numbers)):
        if numbers[i] >= max_num:
            max_num = numbers[i]
    return max_num

def minimum(numbers):
    mini_num = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] <= mini_num:
            mini_num = numbers[i]
    return mini_num


main()




