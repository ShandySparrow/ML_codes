import concurrent.futures

def compute_square(number):
    return number * number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

executor = concurrent.futures.ThreadPoolExecutor()
results = executor.map(compute_square, numbers)

for result in results:
    print(result)

