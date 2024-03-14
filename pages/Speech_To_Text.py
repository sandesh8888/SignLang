from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS 
import os
import pyttsx3 
from langdetect import detect 
import pycountry

all_languages = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az', 'basque', 'eu', 'belarusian', 'be','bengali', 'bn', 'bosnian', 'bs', 'bulgarian','bg', 'catalan', 'ca', 'cebuano','ceb', 'chichewa', 'ny', 'chinese (simplified)', 'zh-cn', 'chinese (traditional)','zh-tw', 'corsican', 'co', 'croatian', 'hr','czech', 'cs', 'danish', 'da', 'dutch','nl', 'english', 'en', 'esperanto', 'eo','estonian', 'et', 'filipino', 'tl', 'finnish','fi', 'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 'georgian', 'ka', 'german','de', 'greek', 'el', 'gujarati', 'gu','haitian creole', 'ht', 'hausa', 'ha','hawaiian', 'haw', 'hebrew', 'he', 'hindi','hi', 'hmong', 'hmn', 'hungarian','hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian','id', 'irish', 'ga', 'italian','it', 'japanese', 'ja', 'javanese', 'jw','kannada', 'kn', 'kazakh', 'kk', 'khmer','km', 'korean', 'ko', 'kurdish (kurmanji)','ku', 'kyrgyz', 'ky', 'lao', 'lo','latin', 'la', 'latvian', 'lv', 'lithuanian','lt', 'luxembourgish', 'lb','macedonian', 'mk', 'malagasy', 'mg', 'malay','ms', 'malayalam', 'ml', 'maltese','mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian','mn', 'myanmar (burmese)', 'my','nepali', 'ne', 'norwegian', 'no', 'odia', 'or','pashto', 'ps', 'persian', 'fa','polish', 'pl', 'portuguese', 'pt', 'punjabi','pa', 'romanian', 'ro', 'russian','ru', 'samoan', 'sm', 'scots gaelic', 'gd','serbian', 'sr', 'sesotho', 'st','shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si','slovak', 'sk', 'slovenian', 'sl','somali', 'so', 'spanish', 'es', 'sundanese','su', 'swahili', 'sw', 'swedish','sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu','te', 'thai', 'th', 'turkish','tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur','ug', 'uzbek', 'uz','vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh','yiddish', 'yi', 'yoruba','yo', 'zulu', 'zu')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def getLangName(lang_code):
    language = pycountry.languages.get(alpha_2 = lang_code)
    return language.name


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"The User said {query}\n")
    except Exception as e:
        print("say that again please.....")
        return "None"
    return query




print ("Welcome to the translator! ")
speak ("Welcome to the translator! ")
print ("Say the sentence you want to translate once you see the word 'listening'")


# Input from user and make input to lowercase
query = takecommand()
while (query == "None"):
    query = takecommand()


from_lang = detect(query)
print ("The user's sentence is in ", getLangName(from_lang))


def destination_language():
    print("Enter the language in which you  want to convert : Ex. Hindi , English , Spanish, etc.")
    print()

    to_lang = takecommand()
    while to_lang == "None":
        to_lang = takecommand()
    to_lang = to_lang.lower()
    return to_lang

to_lang = destination_language()

while (to_lang not in all_languages):
    print("Language in which you are trying to convert is currently not available, please input some other language")
    print()
    to_lang = destination_language()


to_lang = all_languages[all_languages.index(to_lang) + 1]

translator = Translator()
text_to_translate = translator.translate(query, dest=to_lang)


text = text_to_translate.text

speak = gTTS(text=text, lang=to_lang, slow=False)

speak.save("audioCap.mp3")

playsound('audioCap.mp3')
os.remove('audioCap.mp3')

print(text)
