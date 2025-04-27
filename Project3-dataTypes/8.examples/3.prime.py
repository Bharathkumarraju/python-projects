def prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

if __name__ == '__main__':
    number = int(input("enter a number to get prime numbers until to it: "))
    for i in range(2, number+1):
        is_prime = prime(i)
        if is_prime:
            print(i)

