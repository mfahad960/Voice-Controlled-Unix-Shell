import speech_recognition as sr

def listen():
	r = sr.Recognizer()
	mic = sr.Microphone() 		# use the default microphone as the audio source

	with mic as source:
		
		print("Listening...")
		r.adjust_for_ambient_noise(source)  	              # listen for 1 second to calibrate the energy threshold for ambient noise levels
		try:
			audio = r.listen(source, timeout = 3)
		except sr.UnknownValueError:
			print("Unintelligible.")
			return
	try:
		print("You said: " + r.recognize_google(audio))    # recognize speech using Google Speech Recognition
	except LookupError:                            	           # speech is unintelligible
		print("Could not understand input.")
		
listen()