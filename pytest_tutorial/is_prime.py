def is_prime(number):
    """
    Checks if the given number is a prime number
    :param number: int The number to check if it's prime
    :return: True if number is prime
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if not number == i and number % i == 0:
            return False
    return True


def main():
    input_number = int(input("Insert a number to check if it's prime"))
    if is_prime(input_number):
        print(f"{input_number} is prime")
    else:
        print(f"{input_number} is not prime")


if __name__ == '__main__':
    main()
