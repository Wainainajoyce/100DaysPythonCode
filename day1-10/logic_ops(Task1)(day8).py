#Logic operations assignment
#Question 1
#(p∨¬q) and q
#Declarations
p = True
q = False
r = True

#Working
var_z = p or (not q)#True
var_y = var_z and q
print(var_y)#False

#Question 2
#(p or q) not (¬q and ¬p)
#Use previous declarations

#Working
var_x = p or q#True
var_w = (not q) and (not p)#False
var_v = var_x or (not var_w)
print(var_v)#True

#Question 3
#(p ∨ q) ∧ (p or  ¬ q)
#Working
var_u = p or q#True
var_t = p or (not q)#True
var_o = var_u and var_t
print(var_o)#True

#Question 4
#p ∨ (q ∧ r) 
#Working
var_n = q and r #False
var_m = p or var_n
print(var_m) #True

#Question 5
#¬(p ∧ q) ∨ (p ∨ q) 
#Working
var_l = p and q #False
var_k = p or q #True
var_j = (not var_l) or var_k 
print(var_j)#True

print("""
You are amazing Joyce
Kudos on all that you are doing
      """)