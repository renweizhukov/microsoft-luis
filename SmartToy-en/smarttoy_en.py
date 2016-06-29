#!/usr/bin/env python
# -*- coding: utf-8 -*-

import luis

# Use the URL given by LUIS when your application is published.
luisClient = luis.Luis(url='https://api.projectoxford.ai/luis/v1/application?id=475d9ce3-d6a4-4dad-8c4b-62283e6b9c0d&subscription-key=c6afd8ceee6341bd9ccebcd8f8244cbb')

# Ask the user to type a sentence to be analyzed by your LUIS application.
strInput = raw_input('Please type a sentence to be analyzed by LUIS: ')

# Send the sentence to your LUIS application to be analyzed.
analyzeRes = luisClient.analyze(strInput)

# Show all identified intents.
print 'All the identified intents are: '
print analyzeRes.intents

# Show all identified entities.
print 'All the identified entities are: '
print analyzeRes.entities

# Show the highest-scored intent.
bestIntent = analyzeRes.best_intent()
print 'The highest-scored intent is {0} with the score {1}'.format(bestIntent.intent, bestIntent.score)

