
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from pymongo import MongoClient
from googleapiclient.discovery import build



def _connect_mongo(username, password):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb+srv://%s:%s@cluster0.khqzqbq.mongodb.net/?retryWrites=true&w=majority' % (username, password)
        conn = MongoClient(mongo_uri)
    else:
        print("koneksi mongodb gagal")


    return conn



class ActionSearchGoogle(Action):
    def __init__(self):

         db = _connect_mongo(username='skripsiuser', password='skripsi123')['test']
         cursor = db['qnas'].find()
         self.faq =  pd.DataFrame(list(cursor))
        
         qss = list(self.faq['Questions'])
         with open("./data/faq.yml", "wt", encoding="utf-8") as f:
             f.write("nlu: \n- intent: question\n  examples: | \n")
             for q in qss:
                 f.write(f"    - {q}\n")

    def name(self) -> str:
        return "action_search_google"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        
        message = tracker.latest_message.get('text')
        if message.lower().startswith("cek informasi"):
            query = message.replace("cek informasi", "").strip()
            service = build("customsearch", "v1", developerKey="AIzaSyBiRrDiWdY1MfRrFtO5U0NgZfTDIiL-U9k")
            result = service.cse().list(q=query, cx="3bd74cd840a9b9f50", num=3).execute()
            results = result.get("items", [])
            response = ""
            for item in results:
                response += f"{item['title']}\n{item['snippet']}\n{item['link']}\n\n"
            if response:
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("maaf, saya tidak menemukan hasil dari informasi yang anda cari")

        else:
            # dispatcher.utter_message("Sorry, gak tau")
            query = tracker.latest_message['text']
            questions = list(self.faq['Questions'])
            answer = list(self.faq['Answers'])
            Ratios = process.extract(query, questions)
            print(Ratios)

            mathed_question, score = process.extractOne(query,questions, scorer=fuzz.token_set_ratio)

            if score > 50:
                matched_row = self.faq.loc[self.faq['Questions'] == mathed_question,]
                answer = matched_row['Answers'].values[0]
                response = "{} \n".format(answer)
        
            else:
                response = "maaf, saya tidak menemukan jawaban untuk pertanyaan tersebut"

        
            dispatcher.utter_message(response)
