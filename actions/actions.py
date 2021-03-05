# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List,Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from . import excel_read_write
from rasa_sdk.events import AllSlotsReset


class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        excel_read_write.DataStore(tracker.get_slot('name'),tracker.get_slot('gender'),tracker.get_slot('city'),tracker.get_slot('occupation'))

        dispatcher.utter_message(text="data stored successfully..")

class FormDataCollect(FormAction):

    def name(self) -> Text:
        return "Form_Info"

    @staticmethod
    def required_slots(tracker:"Tracker")-> List[Text]:
        return ['name','gender','city','occupation']

    def slot_mappings(self) -> Dict[Text,Union[Dict,List[Dict[Text,Any]]]]:
        return{
            'name':[self.from_text()],
            'gender':[self.from_text()],
            'city':[self.from_text()],
            'occupation':[self.from_text()],
        }

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Here are the information that you are provided would you like to save it?\n Name:{0},\n Gender:{1},\n City:{2},\n Occupation:{3}".format(tracker.get_slot('name'),tracker.get_slot('gender'),tracker.get_slot('city'),tracker.get_slot('occupation')))
        return[]


class ActionFetchData(Action):

    def name(self) -> Text:
        return 'action_fetch_data'

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        output= excel_read_write.Fetchdata(tracker.latest_message['entities'][0]['value'],tracker.latest_message['entities'][1]['value'])
        
        dispatcher.utter_message(text="This the data that you have asked for.\n{}".format(",".join(output)))

class deleteslots(Action):

     def name(self) -> Text:
            return "slot_clear"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         return [AllSlotsReset()]

