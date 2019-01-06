def cheese_and_crackers(cheese_count,box_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"You have {box_of_crackers} boxes of crackers")
    print("man that not enough for party")
    print("Get a blanket \n")
print("we can just give the function numbers directly")
cheese_and_crackers(20,30)
print("Or we can use variables")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print("we can do math insde")
cheese_and_crackers(10  + 20 , 5 + 6)
print("An we can combine the two ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +  1000)