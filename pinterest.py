import os
import requests
from bs4 import BeautifulSoup
from telethon.sync import TelegramClient
from telethon import TelegramClient,events,sync
from telethon.sessions import StringSession
from telethon import functions,types
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import SendMediaRequest
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
string_session = os.environ.get("SESSION")
sudo_users = list()
client = TelegramClient(StringSession(string_session), api_id, api_hash)
client.start()
@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.peer_id.user_id == 1602528719:
        if event.raw_text[0:5] == ".sudo":
            ns = event.raw_text[6:]
            ns = int(ns)
            sudo_users.append(ns)
            print(sudo_users)
        elif event.raw_text[0:6] == ".rsudo":
            ns = event.raw_text[8:]
            ns = int(ns)
            sudo_users.remove(ns)
        elif event.raw_text[0:6] == ".lsudo":
            ns = str(sudo_users)
            ns = ns[1:-1]
            ns = ns.replace(",","\n")
        else:
            pass
    elif event.peer_id.user_id in sudo_users:
        if event.raw_text[0:6] == ".dload":
            url = event.raw_text[7:]
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html5lib')
            suin = str(soup.prettify())
            suin = suin[suin.find('<link as="image"'):suin.find(".jpg")+4]
            lwan = suin[suin.find('"https://i.pinimg.com/')+1:suin.find('.jpg')+4]
            tag = ".jpg"
            for i in lwan:
                if i == " ":
                    lwan = suin[suin.find('"https://i.pinimg.com/')+1:suin.find('.png')+4]
                    tag = ".png"
                    break
                else:
                    pass
            
            imgdata = requests.get(lwan).content
            img = open("img"+tag,"wb")
            img.write(imgdata)
            img.close()
            await client.send_file(event.peer_id.user_id, 'img'+tag, caption="★𝓐𝓟★")
    else:
        await client.send_message(event.peer_id.user_id, "YOU CAN NOT ACCESS THE BOT BECAUSE YOU ARE NOT A MEMBER OF ★𝓐𝓟★")


client.run_until_disconnected()