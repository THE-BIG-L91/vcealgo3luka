def largestPower(n):
    if (n == 1):
        return 0
    elif (n == 2):
        return 1
    
    curr_power = 1
    index = -1 # possible due to the checks up the top
    while (curr_power <= n):
        curr_power*=2
        index += 1

    return index

def numDigits(n): # works in a similar way to largestpower
    if (n < 11):
        return 1    
    smallest_hund = 10
    index = 1 

    # taking a number mod. 10^(length + 1) will give you
    # the number
    # e.g. 123 mod. 1000 = 123

    while (n%smallest_hund != n):
        smallest_hund *= 10
        index += 1
    return index

# accepts a string, n, which represents a binary number
def StringtoDecimal(n):
    length = len(n) - 1
    num = 0

    for i in n:
        if (i=='1'):
            num += 2**length
        length -= 1
    return num


# general gist of how this works
# check if it's zero -- if so, return "0"
# put down a 1 initially (always going to be 1 past the check)
# get the next largest and put in the difference between them in 0s

def StringDecimaltoBinary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    
    curr_n = n
    prev_largest_power = 0
    largest_power = largestPower(curr_n)
    binary_rep = ""

    while (curr_n != 0):
        curr_n -= 2**largest_power
        binary_rep += '1'
        prev_largest_power = largest_power
        largest_power = largestPower(curr_n)
        diff = prev_largest_power - largest_power
        binary_rep += '0'*(diff-1) # -1 so you don't print a 0 where the next 1 is
    
    return binary_rep

def toDecimal(n):
    decrep = n
    binrep = 0

    if decrep % 2 == 1:
        decrep += 1
        binrep -= 1

    i = 1

    while (n != 1):
        n /= 2
        decrep += (2**i)
        i += 1
    
    return decrep

# Revised version -- did not want to use strings
# Works in a vaguely similar way to the version using strings, 
def toBinary(n):
    if (n==0):
        return 0
    if (n==1): 
        return 1
    
    curr_n = n
    largest = largestPower(curr_n)
    binary_rep = 0

    while (curr_n != 0):
        curr_n -= 2**largest
        binary_rep += 10**largest
        largest = largestPower(curr_n)

    return binary_rep

print(toDecimal(1001))
print(toDecimal(1000))
print(toDecimal(10101))
print(toDecimal(11000))

for i in range(0,512):
    binrep = toBinary(i)
    print("Binary: " + str(binrep) + " | Decimal: " + str(i))
