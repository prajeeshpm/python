print("Lets practice everything")
print('You \'d need to know \'bout esapes with \\ that do:')
print('\n newlines and \t tabs.')
poem = """
\t The lovely world
with logic so firmly planted 
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehended passion form intution 
and requires and explanation
\n\t where there is none 
"""
print("------------------")
print(poem)
print("------------------")
Five = 10 - 2 + 3 - 6
print(f"This shoul be five :{Five}")
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)
#rmebember that this another way t format a string 
#print("with a starting point of : {}".format.start_point())
print("with a starting point of : {}".format(start_point))
#its just like with an f"" string "
#print(f"we'd have {beans} bean,   {jars} jars,and {crates} cratest")
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")


start_point = start_point / 10
print("we can also do taht this way:")
formula = secret_formula(start_point)
print(formula)
#This is as an easy 
print("We'd have {}beans,{}jars and {}crates.".format(*formula))