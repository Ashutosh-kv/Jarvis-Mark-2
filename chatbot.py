from rivescript import RiveScript
import pyttsx3, random, smtplib
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[len(voices)-6].id)

def wishMe():
	

def botAsk():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold =  1
		audio = r.listen(source)
	try:
		query = r.recognize_google(audio, language='en-in')
		print('User: ' + query + '\n')

	except sr.UnknownValueError:
		speak('Try again')
		pass

	return query
	print(query)

def speak(audio):
	print(audio)
	engine.say(audio)
	engine.runAndWait()

bot = RiveScript()
bot.load_directory('.\\brain')
bot.sort_replies()

while True:
	msg = botAsk()
	if msg == 'quit':
		exit()

	else:
		reply = bot.reply('localuser', msg)
		text = 'JARVIS:{}\n'.format(reply)
		speak(reply)
