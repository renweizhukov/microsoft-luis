#! python3

from projectoxford.speech import SpeechClient
sc = SpeechClient("0504570918ad49c9af264f1c2d94787e", gender='Female', locale='en-US')
print = sc.print
input = sc.input

from projectoxford.luis import LuisClient
lc = LuisClient("https://api.projectoxford.ai/luis/v1/application?id=5f4fd9aa-b6a6-42a7-90e4-9373b2f631ad&subscription-key=c6afd8ceee6341bd9ccebcd8f8244cbb&q=")

print("Hello, welcome to Mario Pizza Shack")
order = input("How may I help you?")
print("You said:", order)
intent, toppings, _  = lc.query(order)

from projectoxford.speech import join_and

if intent == "Pizza" and toppings:
    print("You will be ordering a pizza with", join_and(toppings))
else:
    print("I am sorry, we only sell pizza here.")

print("Thank you for visiting Mario Pizza Shack")




