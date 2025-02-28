# Polish flag puzzle
Size = 16
polishFlags = []

def Examine(n):
    return polishFlags[n]

def Swap(m,n):
    temp = polishFlags[m]
    polishFlags[m] = polishFlags[n]
    polishFlags[n] = temp

def fill(n): # fill with rand,
    for i in range(0, n):
        polishFlags.append(i%2)

def toCounterRep(n):
    for i in range(0, Size):
        if (n[i] == 0):
            n[i] = "R"
        else:
            n[i] = "W"

def main():
    fill(Size)

    begin = 0
    end = Size - 1 # Begins at zero
    i = 0

    polishFlagsCopy = polishFlags.copy()
    toCounterRep(polishFlagsCopy)
    print(polishFlagsCopy)

    while (begin <= end):
        if Examine(i) == 0:
            Swap(begin, i)
            begin += 1
        else:
            Swap(end,i)
            end -= 1

    toCounterRep(polishFlags)
    print(polishFlags)

main()

# Polish flag problem algorithm:
# In order to sort the algorithm, we must keep track of a pointer to the beginning 
# counter, a pointer to the end counter, and a spare pointer which points to the beginning node initially.

# Then, repeat the following while the pointer to the first counter is less than the pointer to the second counter.
# If the counter pointed to by the beginning counter is less than the counter
# pointed to by the spare pointer's counter, then swap the two counters,
# and increment the beginning pointer by one.

# If this isn't the case, swap the end pointer's counter with the
# spare pointer's counter, and decrement end.

# Polish flag problem pseudocode
# Not too far off from the Python code above

# begin = 0
# size = n - 1
# i = 0

# while (begin <= end) do
    # if Examine(i) == 0 then
    #   Swap(begin, i)
    #   begin = begin + 1
    # else
    #   Swap(end, i)
    #   end = end - 1
    # endif
# endwhile
