import boto3
import json

session = boto3.Session(profile_name='dclouddev')

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('wowquesttracker_questlinesv3')

response = table.scan()

quests = response['Items']

# print(quests)
#
for quest in quests:
    print(quest['quest_name'])
    # print(quest['quest_data'][0])
    # print(quest['quest_data'][1])
    # print(quest['quest_data'][2])


# print(response)
