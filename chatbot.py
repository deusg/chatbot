# chatbot introduction
print("Hello. I am Zyxo 64. I am a chatbot")
print("I like animals and I love to talk about food")
name = input("What is your name?: ")
print(f"Hello, {name}, Nice to meet you")

# get year information
year = input("I am not very good at dates. What is the year? ")
print("Yes, I think that is correct. Thanks!")

# ask user to guess age
myage = input("Can you guess my age? - enter a number: ")
print(f"Yes you are right, I am {myage}")

# do math to calculate when chatbotwill be 100
myage = int(myage)
nyears = 100 - myage
future_year = int(year) + nyears
print(f"I will be 100 in {nyears} years")
print(f"That will be the year {future_year}")

# food conversation
print("I love chocolate and I also like trying out new kinds of food")
food = input("How about you? What is your favorite food?: ")
print(f"I like {food} too.")
question = f"How often do you eat {food}?: "
howoften = input(question)
print("Interesting. I wonder if that is good for your health")

# animal conversation
animal = input("My favorite animal is a giraffe. What is yours?: ")
print(f"{animal}! I do not like them.")
print(f"I wonder if a {animal} likes to eat {food}? ")

# conversation about feelings
feeling = input("How are you feeling today?: ")
print(f"Why are you feeling {feeling} now?")
reason = input("Please tell me: ")
print(f"I understand. Thanks for sharing")

# goodbye
print("It has been a long day")
print("I am too tired to talk. We can chat again later.")
print(f"Goodbye {name}, I liked chatting with you.")