import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text to speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

def listen_and_transcribe():
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        # Read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # Convert the audio to text
        text = r.recognize_google(audio_data)
        return text

def speak(text):
    # Stop speaking if currently speaking
    if engine.isSpeaking():
        engine.stop()
    # Say the text
    engine.say(text)
    # Wait for the speech to complete
    engine.runAndWait()

while True:
    text = listen_and_transcribe()
    print(f"You said: {text}")
    speak(text)