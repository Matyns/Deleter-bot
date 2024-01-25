api_id = 12345678 #insert your api id
api_hash = ''     #insert your api hash
token =''         #insert your bot token

from pyrogram import Client, filters
import logging
import time

logging.basicConfig(
   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
   level=logging.INFO
)
LOGGER = logging.getLogger(__name__) #shows in terminal if the bot is running by showing 'pyrogram.dispatcher - INFO - Started 12 HandlerTasks'

app = Client(
   'deleter', #your bot name(it can be different from the actual name of the bot)
   api_id,
   api_hash,
   token
)


@app.on_message(filters.private)
def start(_,message):
   chat_id = message.chat.id #the ID of the chat between user and bot
   msg_id = message.id       #the ID of the message sent by user
   txt = message.text        
   app.send_message(chat_id,'send number below 10')
   if txt !='/start':
      num = int(txt)
      if num > 10:
         num = 10
      for i in range(num):
         app.send_message(chat_id,f'{i+1}')      #sends messages to user one by one till the number of user or 10 at most

      time.sleep(10)
      for i in range(num+2):
         time.sleep(1)
         app.delete_messages(chat_id,msg_id+i)   #Delets messages one by one from the first number send by user till the last one send by bot

app.run()    #Runs the bot
