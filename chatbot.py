pip install flask nltk transformers torch
# chatbot.py
import random
import nltk
from transformers import pipeline
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

class Chatbot:
    def __init__(self):
        self.qa_pipeline = pipeline("question-answering")
        self.stop_words = set(stopwords.words("english"))
        self.default_responses = [
            "I'm not sure about that. Can you try asking in another way?",
            "Sorry, I don't understand that. Can you rephrase?",
            "Hmm... I don't know. Could you ask something else?"
        ]
        self.greetings = ["hello", "hi", "hey"]
        self.goodbyes = ["bye", "goodbye", "see you"]

    def is_greeting(self, text):
        return any(greet in text for greet in self.greetings)

    def is_goodbye(self, text):
        return any(bye in text for bye in self.goodbyes)

    def get_answer(self, question):
        context = "This is a context for answering questions. Add specific context if you want the chatbot to focus on certain topics."
        try:
            answer = self.qa_pipeline(question=question, context=context)
            return answer['answer']
        except:
            return random.choice(self.default_responses)

    def respond(self, user_input):
        text = user_input.lower()
        if self.is_greeting(text):
            return random.choice(["Hello! How can I help you today?", "Hi there! What can I do for you?"])
        elif self.is_goodbye(text):
            return random.choice(["Goodbye!", "See you later!", "Take care!"])
        else:
            return self.get_answer(user_input)
          
# test_chatbot.py
from chatbot import Chatbot

chatbot = Chatbot()
print(chatbot.respond("Hello"))
print(chatbot.respond("What is artificial intelligence?"))
print(chatbot.respond("Bye"))
