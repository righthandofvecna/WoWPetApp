#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib      import parse as urlParse

from html        import *
from quests      import *


def getOptimalFromQuest(quest):
    if "quest_1" in quest:
        return "bulbasaur"
    elif "quest_2" in quest:
        return "squirtle"
    else:
        return "charmander"

def formatQuestDiv(quest):
    html = "<div><p>" + getOptimalFromQuest(quest) +"</p></div>"
    return html

# HTTPRequestHandler class
class MyServerRequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        ### Serve secondary files
        if self.path == '/favicon.ico':
            f = open('favicon.ico','rb')
            self.reply(f.read(), writeRaw=True)
            f.close()
            return
        if self.path == '/main.css':
            f = open('main.css','rb')
            self.reply(f.read(), contentType='text/css', writeRaw=True)
            f.close()
            return

        ### Serve the main content
        # If there is nothing in the path other than maybe /?,
        # show the landing page!
        if len(self.path) <= 2:
            self.reply(landingPage())
            return
        
        # Otherwise, try to decide what should be displayed
        elif self.path[0:2] == "/?":
            parameters = urlParse.parse_qs(self.path[2::])


            # If the user did not enter a search term
            if self.path == '/?questName=':
                self.reply(landingPage("Please enter a quest name"), responseCode=400)
                return
            
            # If the user searched by quest name:
            elif "questName" in parameters and len(parameters['questName']) > 0:
                questName = parameters["questName"][0]

                # if it is a valid quest, display it
                if isValidQuest(questName):
                    self.reply(questPage(questName))
                    return

                # if it's not a valid quest, say so
                else:
                    self.reply(noSuchQuestPage())
                    return
            
            # Otherwise, just display the landing page
            else:
                self.reply(landingPage("Your request was invalid"), responseCode=400)
                return

        # if nothing has been sent by this point, return a 404
        self.send_response(404)
        return
    
    def reply(self, content, contentType='text/html', responseCode=200, writeRaw=False):
        # send response status code
        self.send_response(responseCode)
        # send headers
        self.send_header('Content-type',contentType)
        self.end_headers()
        if writeRaw:
            self.wfile.write(content)
        else:
            # Write content as utf-8 data
            self.wfile.write(bytes(content, "utf8"))

 
def run():
    try:
        # Server settings
        # Choose port 8080, for port 80, which is normally used for a http server, you need root access
        server_address = ('192.168.0.21', 8081) #('127.0.0.1', 8081)
        httpd = HTTPServer(server_address, MyServerRequestHandler)
        print('running server...')
        httpd.serve_forever()

    except KeyboardInterrupt:
	    print('\n^C received, shutting down the web server')
	    httpd.socket.close()

run()