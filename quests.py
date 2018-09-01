import database

def getQuestFromID(questID):
    return database.db[questID]

def getValidQuestIDs():
    return list(database.db.keys())

def isValidQuest(questID):
    return questID in getValidQuestIDs()