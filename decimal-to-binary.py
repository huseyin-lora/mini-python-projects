# Step 1: Get the decimal number as input from the user
decimal_number = int(input("Enter a decimal number: "))

# Step 2: Initialize an empty string to store the binary representation
binary_representation = ""

# Step 3: Perform the binary conversion manually
while decimal_number > 0:
    remainder = decimal_number % 2  # Get the remainder when divided by 2
    binary_representation = str(remainder) + binary_representation  # Add the remainder to the front of the binary string
    decimal_number //= 2  # Divide the decimal number by 2 and update it

# Step 4: Print the binary representation
print(f"{binary_representation}")
