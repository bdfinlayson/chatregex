import os
import re

from pipeline import book_patterns
from pipeline.pipeline import Pipeline


class PromptProcessor:
    exit_commands = ["nothing", "no", "don't", "stop", "quit", "exit", "goodbye", "bye", "later"]
    file_path: str
    book: str
    pipeline: Pipeline

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
        book_input = input("Hi, which book are you interested in? Your options are: \n- A Study In Scarlet\n- The Secret Adversary\n- The Sign of Four\n\n")
        if re.search(r'study|scarlet', book_input, flags=re.IGNORECASE):
            self.book = 'a_study_in_scarlet'
        elif re.search(r'secret|adversary', book_input, flags=re.IGNORECASE):
            self.book = 'the_secret_adversary'
        elif re.search(r'sign|four', book_input, flags=re.IGNORECASE):
            self.book = 'the_sign_of_four'
        else:
            print("Sorry, we don't have that book. Have a great day!")
            return

        self.file_path = f'{os.getcwd()}/src/chatregex/books/{self.book}.txt'
        book_human_readable = re.sub(r'_', ' ', self.book).title()
        print(f"Awesome! You are interested in {book_human_readable}")

        question = input("Enter a question you have: ")

        self.pipeline = (
            Pipeline()
                .build(self.file_path, book_patterns[self.book])
                .execute()
        )

        self.handle_conversation(question)

    def handle_conversation(self, reply):
        while not self.make_exit(reply):
            reply = self.match_reply(reply)

    def make_exit(self, reply):
        if reply.lower().strip() in self.exit_commands:
            print("Ok, have a great day!")
            return True

        return False

    def match_reply(self, reply):
        for key, values in self.matching_phrases.items():
            for regex_pattern in values:
                found_match = re.match(regex_pattern, reply, flags=re.IGNORECASE)
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
        self.print_answer('investigator')
        return self.prompt_for_question()

    def perpetrator_intent(self):
        self.print_answer('perpetrator')
        return self.prompt_for_question()

    def suspect_intent(self):
        self.print_answer('suspects')
        return self.prompt_for_question()

    def crime_intent(self):
        self.print_answer('crime')
        return self.prompt_for_question()

    def describe_intent(self):
        return input(
            "inside self.describe_intent() - Do you have another question? ")

    def when_intent(self):
        return input("inside self.when_intent() - Do you have another question? ")

    def print_answer(self, subject: str):
        print(self.pipeline.answers[subject], end='\n\n\n')

    def prompt_for_question(self):
        return input(f"Do you have another question?: ")

# Creating and calling ChatRegex
chatbot = PromptProcessor()
chatbot.welcome()
