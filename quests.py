def getOptimalFromQuest(quest):
    if "quest_1" in quest:
        return "bulbasaur"
    elif "quest_2" in quest:
        return "squirtle"
    elif "quest_3" in quest:
        return "charmander"
    else:
        return 'ERROR'

def getValidQuestIDs():
    return ['quest_1','quest_2','quest_3']

def getQuestNameFromID(questID):
    return questID[0].upper() + questID[1::]

def isValidQuest(questID):
    return questID in getValidQuestIDs()