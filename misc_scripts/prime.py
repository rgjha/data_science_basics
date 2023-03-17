import time
start_time = time.time()

def is_prime(n):
    """
    Returns True if the given number n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def checkPrime(n):
	if n<= 1 or n%2 == 0 or n%3 == 0:
		return False
	if n == 2 or n == 3:
		return True

	i = 5  # 6n-1 
	while(i * i <= n):
		if (n%i == 0 or n%(i+2) == 0):   # Check for 6n-1 and 6n+1.
			return False
		i += 6
		return True

#print(is_prime(27985032798461)) 
#print(checkPrime(27985032798461))

# 28116440335967 
#print(is_prime(28116440335967)) 
print(checkPrime(28116440335967))

print("--- %s seconds ---" % (time.time() - start_time))
