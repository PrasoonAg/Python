#=========================================================================#
# 06 - Unary Operators
#=========================================================================#
# A Unary Operator is an operator that works on only one operand (one value/variable).
# Unary Operator
# +x	    (Positive)
# -x	    (Negative)
# not x	    (Logical NOT)  Already covered in Operators
# ~x	    (Bitwise NOT)
#=========================================================================#
a = 5
print(-a) # -5
print(+a) # 5

b = -8
print(+b) # -8
print(-b) # 8
#=========================================================================#
# Clarity of Unary Opertors when dealing with Arthematic Operators.
#=========================================================================#
num = 10

num =+ 20 # num = (+num)
print(num) # 10

num =- 20 # num = (-num)
print (num) # -20
# Num gets assigned with its respected Unary Operator and its new value.
# No Arthematic Operation takes place.
#=========================================================================#