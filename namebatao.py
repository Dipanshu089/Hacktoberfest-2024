def triangle(n):
    return recursive_triangle(n, n)

def recursive_triangle(x, n):
    # First we must verify that both input values are integers.
    if type(x) != int or type(n) != int:
        return 'error'
    # If x is bigger than n, we will still only print the full triangle, so we can set them equal.
    if x > n:
        x = n
    # If either value is zero, the output should be an empty string because there are no lines or triangle to print.
    if x == 0 or n == 0:
        return ''
    # Let's set some variable names to help us out.
    star_print = n
    line_number = x
    # I'll create an empty string that we can concatenate values to.
    line_print = ''

# The difference value will determine how many shapes are needed to fill the line before the stars are printed.
    difference = star_print - line_number
    # If difference is not zero, we will print that value of spaces before the stars. The star print will be the
    # remainder, also known as line number.
    if difference != 0:
        line_print += ' '*difference
        line_print += '*'*line_number
    # If difference is zero, then we can just fill the line with stars.
    else:
        line_print += '*'*star_print
    # If the line number is greater than one, we can return our string and use the recursive call to run the function
    # again with the line number as one value less.
    if line_number > 1:
        return line_print+'\n'+str(recursive_triangle(line_number-1, star_print))
    # If the line number is exactly one, then we don't need to use the recursive call.
    elif line_number == 1:
        return line_print
