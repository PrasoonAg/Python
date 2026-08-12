#=========================================================================#
# Q2 - Find the Line Number of a Word
#=========================================================================#
# WAF to find the line number where the word "learning"
# occurs for the first time.

# Return -1 if the word is not found.
def check_for_line():

    word = "learning"
    line_no = 1
    line = True      # Used to start the while loop.

    with open("practice1.txt", "r") as f:

        # readline() returns an empty string ("") at the end of the file.
        # This automatically stops the loop.
        while line:

            line = f.readline()

            # Check whether the word exists in the current line.
            if word in line:
                return line_no

            line_no += 1

    # Executed only if the word is not found.
    return -1


print(check_for_line())
#=========================================================================#