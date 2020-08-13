from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction



class ComplainForm(FormAction):

    def name(self):
        return "complain_form"

    @staticmethod
    def required_slots(tracker):

        
            return ["complain_type", "complain_text"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
                

            "complain_text": [
                self.from_text(intent="complain"),
            ],



        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

     
     #Writing complin to external file.
        f = open("complaints.txt", "a")
        xp=tracker.get_slot("complain_type")      
        f.write("Complain Area: ")
        f.write(xp)
        f.write(",  Complain Text: ")
        xp=tracker.get_slot("complain_text")   
        f.write(xp)
        f.close()   

        dispatcher.utter_message("Thanks Complain Registered")
        return []
