#Question 1
#(-P ^ - Q) v (Q ^ -R)
#Declaration
# p = True
# q = False
# r = True
# #Working
# var_p = (not p) or (not q)#True
# var_q = q and (not r)#False
# var_a = var_p or var_q
# print(var_a)

#Question 2
#(P v Q )^ ((P^R)) v (Q ^ R)
#Declaration
p = True
q = False
r = True

var_p = p or q#True
var_q = p and r#True

var_b = var_p and var_q

var_r = q or r#True

var_c= var_b or var_r
print(var_c)

#Question 3
#[(p ∨ q) ∧ (r ∨ ¬q)] negative (p ∨ r)]
#declaration
# p = True
# q = False
# r = True

# #Working
# var_p = p or q#True
# var_q = r or (not q)#True

# var_d = var_p and var_q
# var_r = p or r#True

# var_e = var_d or (not var_r)
# print(var_e)





