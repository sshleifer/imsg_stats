# Reads in some tables from chat.db and joins.
# Sam Shleifer, Peter Dewire
# April 8, 2015.

import os
import pandas as pd
import sqlite3
CHAT_DB = os.path.expanduser("~/Library/Messages/chat.db")

# contacts data stored in ~/Library/Application\ Support/ AddressBook
# not sure yet how to use the data (complicated format)
#

###Random Debugging Tools
def find_unis(df):
  unis = {}
  for col in df.columns:
    try:
      unis[col] = len(df[col].unique())
    except TypeError:
      continue
  return unis

def getTabs(c):
  c.execute("SELECT name FROM sqlite_master WHERE type='table';")
  return c.fetchall()

def tbl_to_df(tab_name, con):
  query = "SELECT * from " + tab_name
  df = pd.read_sql(query, con)
  return df

####Read in Chat
def writeChat():
  '''Writes message number,type. text, other person and date to msg.csv'''
  db = sqlite3.connect(CHAT_DB)
  msg = pd.read_sql("SELECT * from message", db)
  chat = pd.read_sql("SELECT * from chat", db)
  cmj =  pd.read_sql("SELECT * from chat_message_join", db)

  full_chat = chat.merge(cmj, left_on='ROWID', right_on='chat_id', how='inner')
  msg_final = pd.merge(msg, full_chat,left_on='ROWID', right_on='message_id')
  keep = ['ROWID_x','text','date','chat_identifier','is_sent']
  print 'Writing', len(msg_final), 'texts to msg.csv...'
  msg_final[keep].to_csv('msg.csv', encoding='utf-8') 
  return msg_final[keep]

def addresses():
  source = os.listdir(os.path.expanduser("~/Library/Application Support/AddressBook/Sources"))[0]
  database = os.path.expanduser(os.path.join("~/Library/Application Support",
    "AddressBook/Sources", source,
    "AddressBook-v22.abcddb"))
  connection = sqlite3.connect(database)
  ad = connection.cursor()
  adtabs = getTabs(ad)
  numtab = pd.read_sql("""SELECT * FROM ZABCDPHONENUMBER
              LEFT OUTER JOIN ZABCDRECORD
              ON ZABCDPHONENUMBER.Z_PK = ZABCDRECORD.Z_PK""", connection)
  nt = numtab[['ZFULLNUMBER','ZFIRSTNAME','ZLASTNAME']]
  nt.colums=['number','fname','lname']
  return nt

def main():
  msg = writeChat()
  nums = addresses()
  mgd = msg.merge(nums, left_on='chat_identifier', right_on='ZFULLNUMBER',
      how='left')
   
if __name__ == '__main__':
    main()
