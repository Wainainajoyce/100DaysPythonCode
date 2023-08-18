#Declarations
a = True
b = False
C = False
p = True
Q = False

#Question 1
#a and  b ∧ ¬c =  a or (b ∧ (¬c))
var_i = a and b#False
var_h = var_i and (not C) #False
var_g = b and (not C) #False
var_f = a or var_g # True
var_h = var_f
print(var_f)
print(var_h)

#Question 2
#(p ∧ q) ∨ (¬p ∧ q) ∨ (¬p ∧ ¬q)
var_e = p and Q #False
var_d = (not p) and Q #False
var_c = (not p) or (not Q) #True
var_b = var_e or var_d #False
var_a = var_b or var_c 
print(var_a) # True


print("You are wonderful.. keep it up!!")



