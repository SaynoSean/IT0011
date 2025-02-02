def pattern_a():
    for i in range(1, 6):
        print(' ' * (5 - i) + ''.join(str(num) for num in range(1, i + 1)))

pattern_a()
def pattern_b():
    i = 1
    while i <= 7:
        print(str(i) * i)
        i += 2

pattern_b()