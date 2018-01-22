import boto3
import json

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('wowquesttracker_questlines')

response = table.scan()

quests = response['Items']

# print(quests)

for quest in quests:
    print(quest)
    for thing,  in quest.items():
        print(thing)

# print(response)
