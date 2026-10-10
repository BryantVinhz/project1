def sortArray(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
def isPrime(n): 
    if n <= 1: 
        return False 
    for i in range(2, n): 
        if n % i == 0: 
            return False 
    return True 

def countPrimes(numbers):
    count = 0
    for num in numbers:
        if isPrime(num):
            count += 1
    return count

input_str = input("Enter a list of numbers separated by space: ") 

numbers = [int(num) for num in input_str.split()] 

print("The list of numbers is:", numbers) 

sortArray(numbers)

if numbers:
    num_to_check = numbers[0] 
    if isPrime(num_to_check): 
        print(f"{num_to_check} is a prime number.") 
    else: 
        print(f"{num_to_check} is not a prime number.")
        
        
# Fix mirror bug