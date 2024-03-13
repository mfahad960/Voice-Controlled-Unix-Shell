import speech_recognition as sr
from gtts import gTTS
import os
import getpass
import playsound
import datetime

def speak(msg):
	tts = gTTS(text=msg, lang='en', slow=False)
	tts.save("msg.mp3")
	playsound.playsound("msg.mp3")
	os.remove('msg.mp3')

def listen():
	r = sr.Recognizer()
	mic = sr.Microphone() 		# use the default microphone as the audio source
	while(1):
		with mic as source:
			print("Listening...")
			speak("Listening...")
			r.adjust_for_ambient_noise(source)  	              # listen for 1 second to calibrate the energy threshold for ambient noise levels

			try:
				audio = r.listen(source, timeout = 3)
			except sr.WaitTimeoutError as e:		      # No audio input provided, timeout initiated
				print("No input detected.")
				speak("No input detected.")
				continue
		try:
			input = r.recognize_google(audio)
			if((input == "exit") or (input == "terminate") or (input == 'close')):
				print("Terminating...")
				speak("Good bye sir")
				break

			print("You said: " + input)    		   # recognize speech using Google Speech Recognition
			speak("You said: " + input)
			commands(input)

		except sr.UnknownValueError:                       # speech is unintelligible
			print("Could not understand input.")
			speak("Could not understand input.")

def commands(cmd):
	if(cmd == "list files" or cmd == "show files"):
		#arr = os.listdir('.')
		print(os.listdir('.'))

	elif(cmd == "current working directory" or cmd == "show current directory" or cmd == "show present directory"):
		print(os.getcwd())

	elif(cmd == "go to home directory"):
		os.system("cd /home")
		print(os.getcwd())

	elif(cmd == "what is the username" or cmd == "username"):
		print("Current user is: " + getpass.getuser())
		speak("Current user is: " + getpass.getuser())

	elif(cmd == "show time" or cmd == "what is the time"):
		dt = datetime.datetime.now()
		print ("The time is: = %s:%s:%s %s" % (dt.strftime("%I"), dt.minute, dt.second, dt.strftime("%p")))
		speak("The time is %s %s %s" % (dt.strftime("%I"), dt.strftime("%M"), dt.strftime("%p")))

	elif(cmd == "show date" or cmd == "what is the date"):
		dt = datetime.datetime.now()
		print ("The date is:  = %s/%s/%s" % (dt.day, dt.month, dt.year))

	elif(cmd == "shutdown"):
		speak("Shutting Down. Goodbye sir.")
		os.system("shutdown -h now")

	elif(cmd == "who created you" or cmd == "name your creator"):
		speak("Fahad created me :)")
		print(":)")

	elif(cmd == "what is your name" or cmd == "who are you"):
		speak("I'm friday")

	else:
		print("Sorry, command does not exist.")
		speak("Sorry, command does not exist.")

	return

listen()