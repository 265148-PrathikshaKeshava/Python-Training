# Prog to separate the prime numbers from the user input

print("Prog separate the prime numbers from the user input")
print("-"*60)


#input
input_numbers = []
print("Enter input values: (! to quit)")
while True:

    user_input = input("->")

    if user_input == '!':
        break

    if user_input.isdigit():
        input_numbers.append(int(user_input))

    

#process
primes = []
# Go through every number
for num in input_numbers:

    # Check if the number is prime and add to primes container
    for i in range(2, num):
        if(num % i == 0):
            break
    else:
        primes.append(num)

# Output

print("-"*80)
print('Primes -> ', *primes)

# Class-assignment:
'''
Upgrade the code to display the minimum and maximum of the list
'''

# check if the number is maximum and display 
print("-"*80)
print("Maximum in the prime number: ", max(primes))

# check if the number is minimum and display 
print("-"*80)
print("minimum in the prime number: ", min(primes))