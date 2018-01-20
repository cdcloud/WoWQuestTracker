import requests
import json


def lambda_handler(event, context):
    # print("In lambda handler")
    print(event)

    character = event["queryStringParameters"]['character']
    realm = event["queryStringParameters"]['realm']
    apikey = "8rh2jpnqadv5j3s83yfrthb6kmsrjjse"

    quest_lines = {
        "Balance of Power": [43496, 40668, 43514, 43517, 43518, 43519, 43581, 43520, 43521, 43522, 43523, 40673, 43525,
                             40675, 43524, 40678, 43526, 40603, 40608, 40613, 40614, 40672, 40615, 43528, 43531, 43530,
                             43532, 43533],
        "Nightfallen But Not Forgotten": [44555, 39986, 39987, 40008, 40123, 40009, 42229, 44672, 40011, 40747, 40748, 
                                          40830, 44691, 40956, 40012, 41149, 40326, 41702, 41704, 41760, 41762, 41834, 
                                          41989, 42079, 42147, 40010, 41028, 40368, 40348, 40370, 41138, 44492, 40324, 
                                          40325, 42224, 42225, 42226, 42227, 42228, 42230],
        "Good Suramarian": [42230, 44636, 44561, 41877, 40746, 41148, 40947, 40745, 42722, 42486, 42487, 42488, 42489,
                            41878, 40727, 40730, 42828, 42829, 42832, 42833, 42834, 42835, 42837, 42836, 42838, 44084,
                            42839, 43969, 42840, 42841, 43352, 42792, 44052, 43309, 43311, 43315, 43313, 43310, 43312,
                            44040, 43317, 43318, 44053, 42490, 43314, 42491, 44562, 44152, 43361, 43360, 44156, 40125,
                            43362, 43502, 43562, 43563, 43564, 43565, 43566, 43567, 43568, 43569]
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
        "Nightfallen But Not Forgotten": ["Khadgar's Discovery", "Magic Message", "Trail of Echoes", 
                                          "The Only Way Out is Through", "The Nightborne Pact", 
                                          "Arcane Thirst", "Shal'Aran", "Ancient Mana", "Oculeth's Workshop", 
                                          "The Delicate Art of Telemancy", "Network Security", "Close Enough", 
                                          "Hungry Work", "Survey Says", "An Old Ally", "A Re-Warding Effort", 
                                          "Scattered Memories", "Written in Stone", "Subject 16", 
                                          "Kel'danath's Legacy", "Sympathizers Among the Shal'dorei", 
                                          "The Masks We Wear", "Blood of My Blood", "Masquerade Masquerade", 
                                          "First Contact", "Tapping the Leylines", "Power Grid  Feeding Shal'Aran", 
                                          "Turtle Powered*", "Something in the Water*", "Purge the Unclean*", 
                                          "Feeding Shal'Aran", "Leyline Apprentice", "Arcane Communion", 
                                          "Scenes from a Memory", "Cloaked in Moonshade", "Breaking the Seal", 
                                          "Moonshade Holdout", "Into the Crevasse", "The Hidden City", 
                                          "The Valewalker's Burden"],
        "Good Suramarian": ["The Valewalker's Burden", "Building an Army", "Seed of Hope", "Lady Lunastre", 
                            "One of the People", "Dispensing Compassion", "Special Delivery", "Shift Change", 
                            "Friends in Cages", "Little One Lost", "Friends On the Outside", "Thalyssra's Abode", 
                            "Thalyssra's Drawers", "The Gondolier", "All Along the Waterways", "Redistribution", 
                            "Moths to a Flame", "Make an Entrance", "The Fruit of Our Efforts", "How It's Made: Arcwine", 
                            "Intense Concentration", "The Old Fashioned Way", "Balance to Spare", "Silkwing Sabotage", 
                            "Reversal", "Vengeance for Margaux", "Seek the Unsavory", "Hired Help", "If Words Don't Work", 
                            "A Big Score", "Asset Security", "Make Your Mark", "And They Will Tremble", 
                            "The Perfect Opportunity", "Or Against Us", "Death Becomes Him", "Rumor Has It", 
                            "Either With Us", "Thinly Veiled Threats", "Vote of Confidence", "In the Bag", 
                            "Ly'leth's Champion", "Friends With Benefits", "The Arcway: Opening the Arcway", 
                            "Court of Stars: Beware the Fury of a Patient Elf", "The Arcway: Long Buried Knowledge", 
                            "Growing Strong", "A Growing Crisis", "Fragments of Disaster", "The Shardmaidens", 
                            "Another Arcan'dor Closes", "Branch of the Arcan'dor", "The Emerald Nightmare: The Stuff of Dreams", 
                            "A Change of Seasons", "Giving It All We've Got", "Ephemeral Manastorm Projector", 
                            "Flow Control", "Bring Home the Beacon", "Withered Progress", "All In", 
                            "Arcan'dor, Gift of the Ancient Magi", "Arluin's Request"]
    }

    body = requests.get(
        "https://us.api.battle.net/wow/character/" + realm + "/" + character + "?fields=quests&locale=en_US&apikey=" + apikey).json()

    all_done = {}
    html_code = ""
    already_ran = 0

    for quest_line, quests in quest_lines.items():
        all_done[quest_line] = {}
        for quest_id in quests:
            if quest_id in body['quests']:
                all_done[quest_line][quest_line_names[quest_line][quests.index(quest_id)]] = True
            else:
                all_done[quest_line][quest_line_names[quest_line][quests.index(quest_id)]] = False

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(all_done)
    }

    return resp