from quests      import *


def insertHead():
    head = '''
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="main.css">
  </head>
'''
    return head

def questPage(quest):
    html = '''
<html>''' + insertHead() + '''
  <body>
    <div>
      <p class="center">
        ''' + getOptimalFromQuest(quest) + '''
      </p>
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
        html = html + '<option value="'+quest+'">'+getQuestNameFromID(quest)+'</option>'
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