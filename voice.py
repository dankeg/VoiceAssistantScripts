#Basic Text to Speech script for voice assistant searches
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 180)
voices = engine.getProperty("voices")
print(voices)
text = "what is the weather today like"
engine.say(text)
# play the speech
engine.runAndWait()

#source env/bin/activate