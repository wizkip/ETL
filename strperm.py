#lets do a simple code to print out all possible permutations of AWS

from itertools import permutations

# A function
def fun(str):

    permlist = permutations(str)

    #iterate through the list

    for perm in list(permlist):

        print(''.join(perm))

if __name__ == "__main__":

    str = "AWS"
    fun(str)

    