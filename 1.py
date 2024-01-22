def quote():
    quote = "‘Don't let the noise of others' opinions\ndrown out your own inner voice.’\n\t\t\t\t\t\t\tSteve Jobs"
    print(quote)

quote()

def between(start, end):
    odd_numbers = []

    for num in range(start, end + 1):
        if num % 2 != 0:
            odd_numbers.append(num)

    return odd_numbers

start = 5
end = 20
odd_numbers = between(start, end)
print(f"{start} and {end} are: {odd_numbers}")

def print_line(length, direction, symbol):
    if direction == 'horizontal':
        return symbol * length
    elif direction == 'vertical':
        return '\n'.join([symbol] * length)
    else:
        return "Неверное направление. Допустимые значения: 'horizontal', 'vertical'"

print(print_line(10, 'horizontal', '*'))
print(print_line(5, 'vertical', '*'))

def max_of_four(a, b, c, d):
    return max(a, b, c, d)
print(max_of_four(1, 2, 3, 4))
print(max_of_four(10, 20, 30, 40))
print(max_of_four(-1, -2, -3, -4))

def sum_in_range(start, end):
    return sum(range(start, end + 1))
print(sum_in_range(1, 4))
print(sum_in_range(5, 7))
print(sum_in_range(-5, -2))


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(2)) # Вывод: True
print(is_prime(4)) # Вывод: False
print(is_prime(29)) # Вывод: True
print(is_prime(33)) # Вывод: False