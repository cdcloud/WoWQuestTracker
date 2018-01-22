import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('wowquesttracker_questlines')

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
                        43362, 43502, 43562, 43563, 43564, 43565, 43566, 43567, 43568, 43569],
    "Insurrection": [45260, 38649, 38695, 38692, 38720, 38694, 42889, 44955, 45261, 44722, 44724, 44723, 44725, 44726,
                     44727, 44814, 45262, 44742, 44752, 44753, 44754, 44756, 45316, 45263, 40391, 43810, 41916, 44831,
                     44834, 44842, 44843, 44844, 44845, 45265, 44743, 44870, 44858, 44928, 44861, 44827, 44829, 44830,
                     44790, 45266, 44739, 44738, 44740, 45317, 45267, 44736, 44822, 45209, 44832, 44833, 45268, 44918,
                     44919, 45063, 45067, 45062, 45065, 45066, 45064, 45269, 44964, 44719, 45417, 45372],
    "Breaching the Tomb": [46730, 46734, 47067, 46286, 46832, 46845, 46499, 46501, 46509, 46510, 46511, 46666, 46245,
                           46772, 46773, 46774, 46244, 46247, 47137, 46251, 47139, 46248, 46252, 46769, 46250, 46249,
                           46246]
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
                        "Arcan'dor, Gift of the Ancient Magi", "Arluin's Request"],
    "Insurrection": ["1. One Day at a Time", "2. Silence in the City", "3. Crackdown", "4. Answering Aggression",
                     "5. No Reason to Stay", "6. Regroup", "7. The Way Back Home", "8. Visitor in Shal'Aran",
                     "1. Continuing the Cure", "2. Disillusioned Defector", "3. Missing Persons",
                     "4. More Like Me", "5. Hostage Situation", "6. In the Business of Souls", "7. Smuggled!",
                     "8. Waning Refuge", "1. A Message from Ly'leth", "2. Tavernkeeper's Fate",
                     "3. Essence Triangulation", "4. On Public Display", "5. Waxing Crescent",
                     "6. Sign of the Dusk Lily", "1. Stabilizing Suramar", "2. Eating Before the Meeting",
                     "3. Take Me To Your Leader", "4. Down to Business", "A Better Future*", "5. Taking a Promenade",
                     "5a. Nullified", "5b. Shield, Meet Spell", "5c. Crystal Clearing", "5d. Powering Down the Portal",
                     "10. Break an Arm", "1. Feeding the Rebellion", "2. Tyrande's Command", "Mouths to Feed*",
                     "3. Trolling Them", "4. Something's Not Quite Right. . . ", "5. Arming the Rebels",
                     "6. Citizens' Army", "7. We Need Weapons", "8. Learning From the Dead", "9. Trial by Demonfire",
                     "1. A United Front", "2. Ready for Battle", "3. Full Might of the Elves", "4. Staging Point",
                     "1. Fighting on All Fronts", "2. Before the Siege", "3. Gates of the Nighthold",
                     "4. Temporal Investigations", "5. Those Scrying Eyes", "6. Scouting the Breach",
                     "7. The Seal's Power", "1. The Advisor and the Arcanist", "2. A Message From Our Enemies",
                     "3. A Challenge From Our Enemies", "4a. The Felsoul Experiments", "5a. Telemantic Expanse",
                     "4b. Resisting Arrest", "5b. Survey the City", "5c. Experimental Instability",
                     "9. Felborne No More", "1. A Taste of Freedom", "2. I'll Just Leave This Here",
                     "3. Breaching the Sanctum", "The Nighthold: Lord of the Shadow Council*", "Fate of the Nightborne*"],
    "Breaching the Tomb": ["1. Armies of Legionfall", "2. Assault on Broken Shore", "3. Seeking Lost Knowledge",
                           "4. Legionfall Supplies", "5. Aalgen Point", "6. Vengeance Point",
                           "7. Spiders, Huh? (Treasure chain)", "7a. Grave Robbin'", "7b. Tomb Raidering",
                           "7c. Ship Graveyard", "7d. We're Treasure Hunters", "7e. The Motherlode",
                           "8. Begin Construction", "8a. The Mage Tower", "8b. The Command Center",
                           "8c. The Nether Disruptor", "9. Altar of the Aegis (Dungeon quest)",
                           "13. Defending Broken Isles", "14. Champions of Legionfall",
                           "15. Shard Times", "16. Mark of the Sentinax", "17. Self-Fulfilling Prophecy",
                           "18. Intolerable Infestation", "19. Relieved of Their Valuables",
                           "20. Take Out the Head...", "21. Championing Our Cause", "22. Strike Them Down"]
}

for key, questline in quest_lines.items():
    for quest in questline:
        # print(quest)
        # print(quest_line_names[key][questline.index(quest)])
        # print(key)
        # print()
        table.put_item(
            Item={
                'quest_id': quest,
                'quest_name': quest_line_names[key][questline.index(quest)],
                'questline': key
            }
        )
