import requests
import json


def lambda_handler(event, context):
    # print("In lambda handler")
    print(event)

    character = 'Draxkal'  # event['character']
    realm = 'Bleeding-Hollow'  # event['realm']
    apikey = "8rh2jpnqadv5j3s83yfrthb6kmsrjjse"

    quest_lines = {
        "Balance of Power": [43496, 40668, 43514, 43517, 43518, 43519, 43581, 43520, 43521, 43522, 43523, 40673, 43525,
                             40675, 43524, 40678, 43526, 40603, 40608, 40613, 40614, 40672, 40615, 43528, 43531, 43530,
                             43532, 43533],
        "balance_of_power2": [43496, 40668, 43514, 43517, 43518, 43519, 43581, 43520, 43521, 43522, 43523, 40673, 43525,
                              40675, 43524, 40678, 43526, 40603, 40608, 40613, 40614, 40672, 40615, 43528, 43531, 43530,
                              43532, 43533]
    }

    quest_line_names = {
        "Balance of Power": ["The Power Within", "The Heart of Zin-Azshari", "A Vainglorious Past", "Fallen Power",
                             "Tempering Darkness", "Lucid Stregnth", "The Wisdom of Patience", "Into Nightmares",
                             "Essence of Power", "Essential Consumption", "Repaid Debt", "Lost Knowledge",
                             "Borrowing Without Asking", "Rite of the Captain", "Literary Perfection", "Twisted Power",
                             "A True Test", "Seeking the Valkyra", "The Mark", "Retrieving the Svalnguard",
                             "A Feast for Odyn", "Presentation is Key", "Odyn's Blessing", "Planning the Assault",
                             "Into the Nighthold", "The Nighthold: Delusions of Grandeur",
                             "The Nighthold: Darkness Calls", "Balance of Power"],
        "balance_of_power2": ["The Power Within", "The Heart of Zin-Azshari", "A Vainglorious Past", "Fallen Power",
                              "Tempering Darkness", "Lucid Stregnth", "The Wisdom of Patience", "Into Nightmares",
                              "Essence of Power", "Essential Consumption", "Repaid Debt", "Lost Knowledge",
                              "Borrowing Without Asking", "Rite of the Captain", "Literary Perfection", "Twisted Power",
                              "A True Test", "Seeking the Valkyra", "The Mark", "Retrieving the Svalnguard",
                              "A Feast for Odyn", "Presentation is Key", "Odyn's Blessing", "Planning the Assault",
                              "Into the Nighthold", "The Nighthold: Delusions of Grandeur",
                              "The Nighthold: Darkness Calls", "Balance of Power"]
    }

    body = requests.get(
        "https://us.api.battle.net/wow/character/" + realm + "/" + character + "?fields=quests&locale=en_US&apikey=" + apikey).json()

    all_done = {}
    html_code = ""
    already_ran = 0

    for quest_line, quests in quest_lines.items():
        if already_ran == 0:
            html_code = html_code + '<table>'
            already_ran = 1
        else:
            html_code = html_code + '</table><table>'

        html_code = html_code + f'<tr><th colspan="2">{quest_line}</th></tr>'
        for quest_id in quests:
            if quest_id in body['quests']:
                html_code = html_code + f'<tr><td>{quest_line_names[quest_line][quests.index(quest_id)]}</td><td>True</td></tr>'
            else:
                html_code = html_code + f'<tr><td>{quest_line_names[quest_line][quests.index(quest_id)]}</td><td>False</td></tr>'
    html_code = html_code + '</table>'

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": html_code
    }

    return resp