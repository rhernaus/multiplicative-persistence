def multiplicative_persistence(number):
    steps = 1
    total = 1
    for i in str(number):
        total = total * int(i)
    # print(f"{steps} - {total}")
    while len(str(total)) > 1:
        steps += 1
        number = total
        total = 1
        for i in str(number):
            total = total * int(i)
        # print(f"{steps} - {total}")
    return steps

max_steps = 0
max_number = 0
for i in range(1, 9999999999999999):
    steps = multiplicative_persistence(i)
    if steps > max_steps:
        max_steps = steps
        max_number = i
        print(f"{max_steps} - {max_number}")
