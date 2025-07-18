from gtts import gTTS 
import os
with open("book.txt", "r", encoding="utf-8") as f:
    text = f.read()

speech = gTTS(text=text, lang='en', slow=False)
speech.save("voice.mp3")
os.system("voice.mp3")