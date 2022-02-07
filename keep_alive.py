from flask import Flask
from threading import Thread

# this is only used for replit and does not need to be added if you are running this client-side
app = Flask('')

@app.route('/')
def home():
    return "Bot is online and pinging"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
