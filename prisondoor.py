# I will use an array ADT to model this problem.
# This array will have 500 values, all equal to zero to begin with.

# Sorry about the pseudocode style.. I'm not overly sure how I should be writing it, so I've done it in a weird mix between C and the pseudocode in Methods.
# * I say this because looking through Lesson 1 -- there are multiple ways suggested as to how you can structure your pseudocode.. I'm just confused
# as to whether Algorithmics has a specific style which they want, or if you can just write it in any way so long as it makes sense.

# Note: The function mod(a,b) is equivalent to a mod b
# Pseudocode:

# cells = {}

# for (i=0, i < 500, i = i + 1) do
#   cells[i] = 0
# end

# i = 1

# while (i <= 500) do
#   for (j=0, j<= 500, j = j + 1) do
        #if (mod(cells[j], i) == 0) then
            # if (cells[j] == 0) then
            #   cells[j] = 1
            # else
            #   cells[j] = 0 
            # ifend
        #ifend
#   forend

#   i = i + 1
# whileend

# Python code
def populate_cells(amt_cells):
    arr = {}
    for i in range(1,amt_cells + 1):
        arr[i] = 0
    return arr

def alg_w3_test(cells):
    print(cells)
    print(cells[225] == 1)
    print(cells[484] == 1)
    print(cells[170] == 0)
    print(cells[499] == 0)
        
def prison_door_problem(amt_cells, iterations):
    cells = populate_cells(amt_cells)
    i = 1

    while (i <= iterations + 1):
        for j in range(1,amt_cells + 1):
            if ((j % i) == 0):
                if cells[j] == 0:
                    cells[j] = 1
                else:
                    cells[j] = 0
        i = i + 1

    alg_w3_test(cells)

def main():
    iterations = 500
    amt_cells = 500

    prison_door_problem(amt_cells, iterations)

main()