#=========================================================================#
# Q1 - Create a File, Replace Text & Search for a Word
#=========================================================================#

# Create a new file "practice1.txt" and add the following data:

# Hi everyone
# we are learning File I/O
# using Java
# I like programming in Java.

# Replace all occurrences of "Java" with "python".
# (Read the file -> Replace the text -> Overwrite the file.)

# Search whether the word "learning" exists in the file or not.

#=========================================================================#
# Replace "Java" with "python"
#=========================================================================#
def replace_java_with_python():

    # Create the file and write the initial content.
    with open("practice1.txt", "w") as f:
        f.write(
            "Hi everyone\n"
            "we are learning File I/O\n"
            "using Java\n"
            "I like programming in Java."
        )

    # Read the file.
    with open("practice1.txt", "r") as f:
        data = f.read()

    # replace() works because read() returns the file contents as a string.
    # It is case-sensitive, so "Java" and "java" are treated differently.
    new_data = data.replace("Java", "python")

    print(new_data)

    # Overwrite the file with the updated content.
    with open("practice1.txt", "w") as f:
        f.write(new_data)


#=========================================================================#
# Search for a Word
#=========================================================================#
def check_for_word():

    word = "learning"

    with open("practice1.txt", "r") as f:
        data = f.read()

    # Method 1 (Recommended)
    if word in data:
        print("Word Found")
    else:
        print("Word Not Found")

    # Method 2
    # find() returns the index if the word is found,
    # otherwise it returns -1.

    # if data.find(word) != -1:
    #     print("Word Found")
    # else:
    #     print("Word Not Found")
#=========================================================================#