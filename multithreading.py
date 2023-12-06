import threading
import time
import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text to speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Flag to indicate whether to stop speaking
stop_speaking = False

def listen_and_transcribe():
    global stop_speaking
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # Convert the audio to text
        text = r.recognize_google(audio_data)
        stop_speaking = True  # Set the flag to stop speaking
        return text

def speak(text):
    global stop_speaking
    # Say the text
    for word in text.split():
        if stop_speaking:
            break
        engine.say(word)
        engine.runAndWait()
    stop_speaking = False  # Reset the flag

while True:
    text = listen_and_transcribe()
    print(f"You said: {text}")
    # Start speaking in a new thread
    threading.Thread(target=speak, args=(text,)).start()
    time.sleep(0.1)  # Sleep for a short time to allow the speaking thread to start
