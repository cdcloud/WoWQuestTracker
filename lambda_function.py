import boto3
import json
import requests
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    # Connect to Dynamo Resource
    dynamodb = boto3.resource('dynamodb')
    # Connect to Table
    table = dynamodb.Table('wowquesttracker_questlinesv3')

    # Set information for Blizzard API Call
    character = event["queryStringParameters"]['character']
    realm = event["queryStringParameters"]['realm']
    apikey = "8rh2jpnqadv5j3s83yfrthb6kmsrjjse"

    # Make API Call to Blizzard for all Quests completed on NA Realms
    body = requests.get(
        "https://us.api.battle.net/wow/character/" + realm + "/" + character + "?fields=quests&locale=en_US&apikey=" + apikey)

    if body.status_code != 200:
        # Form return response with Error code and response
        resp = {
            "statusCode": body.status_code,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(body.json())
        }
        return resp

    # Jsonify the object
    body = body.json()

    # Set Character class
    character_class = body['class']
    # Set Character Faction
    character_faction = body['faction']

    # Scan entire Table for items
    response = table.scan(
        FilterExpression=Attr('faction').contains(character_faction) & Attr('class').contains(character_class)
    )
    # Grab just the 'Items' from the data as its all we care about
    quests = response['Items']

    # Create empty Dict to store completed status in to be returned to the frontend
    all_done = {}

    # Loop through items pulled from Dynamo
    for quest in quests:
        # Store off relevant information for easier use
        quest_line = quest['quest_line']
        quest_order = int(quest['quest_order'])
        quest_name = quest['quest_name']
        quest_id = int(quest['quest_id'])

        # Check if the quest_line key has been created before ot not
        # Create it if it has not, move on if it has
        if quest_line not in all_done:
            all_done[quest_line] = {}

        # Check if quest id in questline is in the data Blizzard returned
        if quest_id in body['quests']:
            # Quest has been completed by character
            all_done[quest_line][quest_name] = True
        else:
            # Quest has not been completed by character
            all_done[quest_line][quest_name] = False

    # Form return response with completion data in body
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(all_done)
    }

    # print(json.dumps(all_done, indent=4))

    return resp
