import os
import openai
import playsound
import speech_recognition as sr
import beepy as beep
from gtts import gTTS
from cleantext import clean


# miscellaneous
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

##################
# Authentication #
##################
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FINE_TUNED_MODEL = os.getenv("FINE_TUNED_MODEL")
BASE_MODEL = os.getenv("BASE_MODEL")

##############
# Functions #
##############

def speak(text):
    if len(text)!=0:
        tts = gTTS(text=text,lang="en")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)

def text_cleaning(text):
    text = clean(text,lower=False,no_line_breaks=False)
    sentences = text.split(". ")
    if len(sentences)==1:
        text = sentences[0]
    else:
        text = ". ".join(text.split(". ")[:-1]) + "."
    clean_text = text.strip()
    return clean_text

def gpt3_fine_tuned(stext,temp,token):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        model = FINE_TUNED_MODEL,
        prompt = stext,
        temperature = temp,
        max_tokens = token,
        top_p = 0,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    content = response.choices[0].text
    content = text_cleaning(content)
    return content

def answer_fine_tuned(text,temp,token):
    lct = text.lower()
    if lct=="":
        response = ""
    elif ("hello" in lct): 
        response = "Hello!"
    elif ("your name" in lct) or ("who are you" in lct):
        response = "People call me Corona Devi. I am the goddess of coronavirus disease."
    elif ("thank you" in lct) or ("thanks" in lct):
        response = "Thank you and goodbye!" 
    else:
        response = gpt3_fine_tuned(text,temp,token)
    return response

def gpt3_base(stext,temp,token):
    openai.api_key = OPENAI_API_KEY
    response = openai.Completion.create(
        engine = "text-curie-001",
        prompt = stext,
        temperature = temp,
        max_tokens = token,
        top_p = 0,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    content = response.choices[0].text
    content = text_cleaning(content)
    return content

def answer_base(text,temp,token):
    lct = text.lower()
    if lct=="":
        response = ""
    else:
        response = gpt3_base(text,temp,token)
    return response