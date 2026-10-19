def even_integers() -> list[int]:
    number_input = int(input("Enter an integer: "))
    return [x for x in range(2, number_input + 1) if x % 2 == 0]

print(even_integers())