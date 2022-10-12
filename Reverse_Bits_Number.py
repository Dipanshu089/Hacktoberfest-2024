
def reverseBits(n) :

    rev = 0

    # traversing bits of 'n' from the right

    while (n > 0) :


        # bitwise left shift 'rev' by 1

        rev = rev << 1

        # if current bit is '1'

        if (n & 1 == 1) :

            rev = rev ^ 1

        # bitwise right shift 'n' by 1

        n = n >> 1

    return rev

n = 11

print(reverseBits(n))
