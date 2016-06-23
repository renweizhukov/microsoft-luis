#!/usr/bin/env python3

from projectoxford.speech import SpeechClient
sc = SpeechClient("0504570918ad49c9af264f1c2d94787e", gender='Male', locale='en-US')
print = sc.print
input = sc.input

print("Hello, welcome to Mario Pizza Shack")
order = input("How may I help you?")
print("You said:", order)
print("Thank you for visiting Mario Pizza Shack")
