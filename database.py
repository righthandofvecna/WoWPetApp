from dataClasses import Pet, Quest


def makeID(questname):
    return questname.replace(' ', '_').replace("'", '').replace("?", '').replace(",", '').replace("!", '').lower()

def addToDB (db, quest):
    db[makeID(quest.name)] = quest


db = {}
addToDB(db, Quest("That's a Big Carcass",
                  [Pet("Chi-Chi", "2 2 1", "Any"),
                   Pet("Pet2", "1 1 1", "Any"),
                   Pet("Jade Owl", "1 * 1", "Any")],
                  [("Turn 1", "use Ethereal"),
                   ("Turn 2", "use Tranquility"),
                   ("Turn 3", "use Alpha Strike"),
                   ("Turn 4", "use Alpha Strike"),
                   ("Turn 5", "use Tranquility"),
                   ("Turn 6+", "use Alpha Strike until Fungus dies")]))

addToDB(db, Quest("Strange Looking Dogs",
                  [Pet("Frog", "2 1 2", "12, 8, 5"),
                   Pet("Garden Frog", "2 1 2", "12, 8, 5"),
                   Pet("Spotted Bell Frog", "2 1 2", "12, 8, 5")],
                  [("", "Keep Swarm of Flies up"),
                   ("", "Heal on CD, unless your pet isn't hurt"),
                   ("", "Otherwise, Tongue Lash")]))


addToDB(db, Quest("Rogue Azerite",
                  [Pet("Sprite Darter Hatchling", "2 1 1", "Any"),
                   Pet("Eternal Strider", "1 2 2", "Any"),
                   Pet("Scooter the Snail", "2 1 1", "Any")],
                  [("", "2, 3 (restart on miss), 1, 1, 1"),
                   ("", "First pet dies"),
                   ("", "2, 1, 1, 1"),
                   ("", "When Sprite Darter Hatchling dies, swap to Eternal Strider"),
                   ("", "1, 2, 3, 1, 3, 1"),
                   ("", "When Eternal Strider dies, swap to Scooter"),
                   ("", "2, 3, 1, 1, 2, 1, 3")]))

addToDB(db, Quest("Quest",
                  [Pet("Pet1", "1 1 1", "Any"),
                   Pet("Pet2", "1 1 1", "Any"),
                   Pet("Pet3", "1 1 1", "Any")],
                  [("Turn 1", "use Skill"),
                   ("Turn 2", "use Skill"),
                   ("Turn 3", "use Skill"),
                   ("Turn 4", "use Skill"),
                   ("Turn 5", "use Skill"),
                   ("Turn 6", "use Skill")]))


