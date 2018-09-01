from quests      import *


def insertHead():
    head = '''
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="main.css">
  </head>
'''
    return head

def questPage(questID):
    quest = getQuestFromID(questID)

    def petTable(pets):
        pet_html = '''
<table class="pets">
  <tr class="pet">'''
        for p in pets:
            pet_html = pet_html + '<td class="petName">'+ p.name +'</td>'
        pet_html = pet_html + '</tr><tr class="pet">'
        for p in pets:
            pet_html = pet_html + '<td class="petSkills"><span class="lbl">Skills:</span> '+ p.skills +'</td>'
        pet_html = pet_html + '</tr><tr class="pet">'
        for p in pets:
            pet_html = pet_html + '<td class="petBreed"><span class="lbl">Breed:</span> '+ p.breed +'</td>'
        pet_html = pet_html + '''
  </tr>
</table>
'''
        return pet_html

    html = '''
<html>''' + insertHead() + '''
  <body>
    <div>
      <h1>
        ''' + quest.name + '''
      </h1>
      ''' + petTable(quest.pets) + '''
      <div class="strategy">
        <table>'''
    for strat in quest.strategy:
        html = html + '<tr><td class="step">' + strat[0] + '</td><td class="strat">' + strat[1] + '</td></tr>\n'
    html = html + '''
        </table>
      </div>
    </div>
    <div>
      <form action="/" method="get">
        <p class="center">
          <input type="submit" value="Return" class="submit">
        </p>
      </form>
    </div>
  </body>
</html>
'''
    return html



def landingPage(message=None):
    html = '''
<html>''' + insertHead() + '''
  <body>
    <h1>Search by Quest</h1>'''
    if message is not None:
        html = html + '<p class="alert center">'+message+'</p>'
    html = html + '''
    <form action="/" method="get">
      <p class="center">
        <label for="questName">Quest: </label>
        <select name="questName" size=1 class="search">
          <option value="" selected disabled hidden>Select Quest</option>'''
    for quest in getValidQuestIDs():
        html = html + '<option value="'+quest+'">'+getQuestFromID(quest).name+'</option>'
    html = html + '''
        </select>
      </p>
      <p class="center">
        <input type="submit" value="Select" class="submit">
      </p>
    </form>
  <body>
</html>'''
    return html


def noSuchQuestPage():
    html = '''
<html>''' + insertHead() + '''
  <body>
    <p class="alert center">No Such Quest Exists</p>
    <form action="/" method="get">
      <p class="center">
        <input type="submit" value="Return" class="submit">
      </p>
    </form>
  <body>
</html>'''
    return html