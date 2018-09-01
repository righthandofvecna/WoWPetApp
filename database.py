from .petBattleHelper import Pet, Quest


def addToDB (db, quest):
    db[quest.name] = quest


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


