#=========================================================================#
# 05 - Multiple Inheritance
#=========================================================================#
# One Child Class inherits from multiple Parent Classes.
# Parent A ──┐
#            ├── Child C
# Parent B ──┘

class A:
    varA = "Welcome to Class A"

class B:
    varB = "Welcome to Class B"

# C inherits from both A and B
class C(A, B):
    varC = "Welcome to Class C"

c1 = C()

print(c1.varC)  # From C
print(c1.varA)  # Inherited from A
print(c1.varB)  # Inherited from B
#=========================================================================#