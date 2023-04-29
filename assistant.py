import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause threshold to adjust for different speech speeds
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return listen()
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the speech recognition service.")
        return None

def process_command(command):
    if "hello" in command:
        speak("Hello there!")
    elif "how are you" in command:
        speak("I'm doing great. Thanks for asking!")
    elif "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        exit()
    else:
        speak("I'm sorry, I don't understand that command.")

# Main loop
while True:
    command = listen()
    if command:
        process_command(command)
