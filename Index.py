import nltk
from nltk.chat.util import Chat, reflections
reflections
{'i am': 'you are',
     'i was': 'you were',
     'i': 'you',
     "i'm": 'you are',
     "i'd": 'you would',
     "i've": 'you have',
     "i'll": 'you will',
     'my': 'your',
     'you are': 'I am',
     'you were': 'I was',
     "you've": 'I have',
     "you'll": 'I will',
     'your': 'my',
     'yours': 'mine',
     'you': 'me',
     'me': 'you'}
set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["You can call me a Cookiebot",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?",]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn python, can you suggest?", "i am looking for python training platforms",]
    ],
    [
        r"i'm doing good ",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn python, can you suggest?",
        ["Pluralsight is a great option to learn python for beginners. You can check their website",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"Bye",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatbot():
        print("Hi, I'm the Cookiebot built by Tina Gurung") 
        chat = Chat(set_pairs, reflections)
        chat.converse()

if __name__ == "__main__":
    chatbot()

