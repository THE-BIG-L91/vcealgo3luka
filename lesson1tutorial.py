import random
import math

def main():
    first = random.randint(1,50)
    second = random.randint(1,50)

    print("My random numbers are:", first, second)

    larger = max(first,second)
    smaller = min(first,second)

    if larger%2 == 0:
        print(larger," is even")
    else:
        print(larger, " is odd")

    if smaller%2 == 0:
        print(smaller, " is even")
    else:
        print(smaller, " is odd")


    if larger%smaller == 0:
        print("Larger is completely divisible by smaller")
    else:
        print("Remainder: ", larger%smaller)

    shorter_side = math.sqrt(larger**2 - smaller**2)

main()
