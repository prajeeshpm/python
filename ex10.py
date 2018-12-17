from sys import argv
script, user_name = argv
prompt = '>'
print(f"Hi {user_name}, i am the {script}.")
print("i'd like to ask you few questions")
print(f"do you like me {user_name}")
likes = input(prompt)
print(f"where do you live {user_name}?")
lives = input(prompt)
print(f"what kind of computer do you have")
computer = input(prompt)
print(f"""
All right so you {likes} . Not sure whaere that is 
you lives in {lives}. Not sure where that is 
Ans you have a {computer} COMPUTER . nICE
""")