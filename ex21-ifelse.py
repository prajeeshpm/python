people = 30
cars = 40
trucks = 15
if cars > people:
    print("we should take cars{}".format(people))
elif cars < people:
    print("we should not take cars")
else:
    print("We cant decide")
if trucks > cars:
    print("Thats too many trucks")
elif trucks < cars:
    print("may be could take the trucks")
else:
    print("We still cant decide")
if people > trucks:
    print("Alright , lets just take the trucks")
else:
    print("fine Lets stay home then")

