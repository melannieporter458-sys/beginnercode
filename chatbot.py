import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and response
pairs = [
    [
        r"my name is(.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!","Hey there!",]
    ],
    [
        r"what is your name?",
        ["I'm a bot, you can call me Chatty.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "It was nice talking to you."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you."]
    ],
 ]

def chatbot():
     print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
     chat= Chat(pairs, reflections)
     chat.converse()

if __name__== "__main__":
     chatbot()
