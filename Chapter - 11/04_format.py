#=========================================================================#
# 04 - Format() Methods (Strings)
#=========================================================================#
# format() inserts values into placeholders {} inside a string.
# Syntax:
# template.format(p1,p2)

a = "{0} is a good {1}.".format("Prasoon","boy")
# Numbers inside {} refer to the position of arguments passed to format().
print(a)

# format() is an older alternative to f-strings and is still widely used.
#=========================================================================#