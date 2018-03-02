import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

session = boto3.Session(profile_name='dclouddev')

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('wowquesttracker_questlinesv3')

response = table.scan(
    FilterExpression=Attr('faction').contains(1) & Attr('class').contains(2)
)

quests = response['Items']

print(quests)
#
# for quest in quests:
#     print(quest['quest_name'])
    # print(quest['quest_data'][0])
    # print(quest['quest_data'][1])
    # print(quest['quest_data'][2])


# print(response)
