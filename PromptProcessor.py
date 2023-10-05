import re


class PromptProcessor:
    negative_responses = ("nothing", "no", "don't", "stop")

    exit_commands = ("quit", "exit", "goodbye", "bye", "later")

    def __init__(self):
        self.matching_phrases = {
            'investigator': [r'.*who.*investigator.*'],
            'perpetrator': [r'.*who.*perpetrator.*'],
            'suspect': [r'.*when.*suspects?.*'],
            'crime': [r'when.*crime.*'],
            'describe': [r'[Dd]escribe when the.*'],
            'when': [r'[Ww]hen.*the.*', r'[Tt]ell me when.*the.*']
        }

    def welcome(self):
        question = input("Hi, enter a question you have: ")

        if question in self.negative_responses:
            print("Ok, have a great day!")
            return

        self.handle_conversation(question)

    def handle_conversation(self, reply):
        while not self.make_exit(reply):
            reply = self.match_reply(reply)

    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Ok, have a great day!")
                return True

        return False

    def match_reply(self, reply):
        for key, values in self.matching_phrases.items():
            for regex_pattern in values:
                found_match = re.match(regex_pattern, reply)
                if found_match and key == "investigator":
                    return self.investigator_intent()
                elif found_match and key == "perpetrator":
                    return self.perpetrator_intent()
                elif found_match and key == "suspect":
                    return self.suspect_intent()
                elif found_match and key == "crime":
                    return self.crime_intent()
                elif found_match and key == "describe":
                    return self.describe_intent()
                elif found_match and key == "when":
                    return self.when_intent()

        return input(
            "I did not understand you. Can you please ask your question again? ")

    # Different intents based on prompt response
    def investigator_intent(self):
        return input(
            "inside self.investigator_intent() - Do you have another question? ")

    def perpetrator_intent(self):
        return input(
            "inside self.perpetrator_intent() - Do you have another question? ")

    def suspect_intent(self):
        return input(
            "inside self.suspect_intent() - Do you have another question? ")

    def crime_intent(self):
        return input("inside self.crime_intent() - Do you have another question? ")

    def describe_intent(self):
        return input(
            "inside self.describe_intent() - Do you have another question? ")

    def when_intent(self):
        return input("inside self.when_intent() - Do you have another question? ")


# Creating and calling ChatRegex
chatbot = PromptProcessor()
chatbot.welcome()
