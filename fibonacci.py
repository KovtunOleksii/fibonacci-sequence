def is_fibonacci_number(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    return a == num

# Введене число для перевірки
input_number = int(input("Введіть число: "))

if is_fibonacci_number(input_number):
    print(f"{input_number} є числом Фібоначчі.")
else:
    print(f"{input_number} не є числом Фібоначчі.")
