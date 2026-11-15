#=========================================================================#
# 02 - Reproduce the Bug
#=========================================================================#
# Some bugs are sneaky, they only occur under certain conditions. In order
# to debug them, we need to be able to reliably reproduce the bug and diagnose
# our problem to figure out which conditions trigger the bug.

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6 )
dice_num = 6 # error - out of index
dice_num = randint(1,5) # solution
print(dice_images[dice_num])

# Change the code so that it always produces the occasional error.
#=========================================================================#