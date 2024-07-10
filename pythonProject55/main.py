import pickle

try:
    # Take integer input from the user
    n = int(input("Enter an integer: "))

    # Take the operation input from the user
    z = input("Enter operation (add, subtract, mul, division): ")

    # Perform the operation based on the input
    if z == "add":
        result = n + 1000
    elif z == "subtract":
        result = n - n+1000  # This will always be 0, corrected to just show subtraction
    elif z == "mul":
        result = n * n*2
    elif z == "division":
        if n != 0:
            result = (n / n )*1 # Correcting to division instead of modulo
        else:
            result = "Division by zero is not allowed"
    else:
        result = "Invalid operation"

    # Print the result of the operation
    print("Result:", result)

    # Save the integer 'n' to a file using pickle
    with open("main.pkl", mode="wb") as pickle_out:
        pickle.dump(n, pickle_out)

    # Confirmation message
    print("Model saved successfully")

except ValueError:
    print("Invalid input. Please enter an integer.")
