import threading
import speech_recognition as sr
import pyttsx3

class SpeechAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.text_to_speech = pyttsx3.init()
        self.is_interrupted = False
        self.lock = threading.Lock()

    def listen_user_input(self):
        with sr.Microphone() as source:
            print("Listening for user input...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        print("Processing user input...")

        try:
            user_input = self.recognizer.recognize_google(audio)
            print("User said:", user_input)

            with self.lock:
                if "stop" in user_input.lower():
                    print("Interrupting...")
                    self.is_interrupted = True

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")

    def say_something(self, text):
        print("Speaking:", text)
        with self.lock:
            self.text_to_speech.say(text)
            self.text_to_speech.runAndWait()

    def assistant_loop(self):
        while True:
            self.listen_user_input()

            with self.lock:
                if not self.is_interrupted:
                    # Replace the following line with your desired text
                    self.say_something("Hello! How can I help you?")

                    # Reset interruption flag
                    self.is_interrupted = False

if __name__ == "__main__":
    speech_assistant = SpeechAssistant()

    # Create a thread for the assistant loop
    assistant_thread = threading.Thread(target=speech_assistant.assistant_loop)

    # Start the assistant thread
    assistant_thread.start()

    # Wait for the assistant thread to finish (this won't happen in this example)
    assistant_thread.join()
