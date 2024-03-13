from gtts import gTTS
import playsound

def speak(msg):
	tts = gTTS(text=msg, lang='en', slow=False)
	tts.save("msg.mp3")
	playsound.playsound("msg.mp3")

speak('abc')