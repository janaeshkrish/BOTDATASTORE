# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#DB connections
from . import data1

#Excel data store
from . import excel

class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # excel.DataStore(tracker.get_slot("name"),
        #     tracker.get_slot("number"),
        #     tracker.get_slot("email"),
        #     tracker.get_slot("occupation"))
        data1.DataUpdate(tracker.get_slot("name"),
        tracker.get_slot("number"),
        tracker.get_slot("email"),
        tracker.get_slot("occupation"))

        dispatcher.utter_message(text="Data Stored Successfully.")

        return []

class ActionFetchData(Action):

    def name(self) -> Text:
        return "action_fetch_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # output=excel.FetchData(tracker.latest_message['entities'][0]['value'],
        #                  tracker.latest_message['entities'][1]['value'])
        output = data1.DataGet(tracker.latest_message['entities'][0]['value'],tracker.latest_message['entities'][1]['value'])
        dispatcher.utter_message(text="This is the data that you asked for, \n{}".format(",".join(output)))

        return []

class FormDataCollect(FormAction):
    def name(self) -> Text:
        return "Form_Info"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["name","number","email","occupation"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict[Text, Any]]]]:
        return {
            "name":[self.from_text()],
            "number":[self.from_entity(entity="number")],
            "email":[self.from_entity(entity="email")],
            "occupation":[self.from_text()]
        }

class DisplayData(Action):

    def name(self) -> Text:
        return "Display_Data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Here are the information that you provided. Do you want to save it?\nName: {0},\nMobile Number: {1},\nEmail: {2},\nOccupation: {3}".format(
            tracker.get_slot("name"),
            tracker.get_slot("number"),
            tracker.get_slot("email"),
            tracker.get_slot("occupation"),

        ))

        return []

    


