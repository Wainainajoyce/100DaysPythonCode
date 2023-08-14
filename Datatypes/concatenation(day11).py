#concatenation combines one or more strings together
#Basically, basically, one can use the + sign or the join() method

#using the + sign
stat1 = "Queen Victoria is the first queen of Great Britain."
stat2 = "She gifted her grandson , emperor of Germany, Mt.Kilimanjaro"

stat3 = stat1 + stat2
print(stat3)

#using the join method
stat4 = ''.join([stat1,stat2])#This separator is used to join the strings into one string hence its a requirement in the join method.
print(stat4)


#The title method converts all the words first letters to capital
him = "He is pissed"
print(him.title())



