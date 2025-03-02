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
