def calculateLeastCommonMultiple(a, b):
    # Print greatest common divisor of the two numbers
    print("The greatest common divisor of {} and {} is {}".format(a, b, calculateGreatestCommonDivisor(a, b)))
    return (a * b) / calculateGreatestCommonDivisor(a, b)

def calculateGreatestCommonDivisor(a, b):
    if b == 0:
        return a
    else:
        return calculateGreatestCommonDivisor(b, a % b)

def main():
    # Calculate the least common multiple of two numbers based on user input
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The least common multiple of {} and {} is {}".format(a, b, calculateLeastCommonMultiple(a, b)))
    
main()