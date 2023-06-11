from multiprocessing import Pool


def worker(number):
    steps = multiplicative_persistence(number)
    return (steps, number)

def multiplicative_persistence(number):
    steps = 0
    while number > 9:
        steps += 1
        product = 1
        while number:
            product *= number % 10
            number //= 10
            if product == 0:
                break
        number = product
    return steps

if __name__ == '__main__':
    max_steps = 0
    max_number = 0
    with Pool() as pool:
        for steps, number in pool.imap_unordered(worker, range(1, 9999999999999999), chunksize = 100000):
            if steps > max_steps:
                max_steps = steps
                max_number = number
                print(f"{max_steps} - {max_number}")