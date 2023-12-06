import speech_recognition as sr
import pyttsx3

class ConversationHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.text_to_speech = pyttsx3.init()
        self.is_interrupted = False

    def listen_and_repeat(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source, timeout=10)  # Adjust timeout as needed

        print("Processing...")

        try:
            text = self.recognizer.recognize_google(audio)
            print("You said:", text)

            if self.is_interrupted:
                print("You interrupted me!")

            self.text_to_speech.say(text)
            self.text_to_speech.runAndWait()

            # Reset interruption flag
            self.is_interrupted = False

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")

        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    def handle_interrupt(self):
        # Set interruption flag
        self.is_interrupted = True

if __name__ == "__main__":
    conversation_handler = ConversationHandler()

    while True:
        conversation_handler.listen_and_repeat()
        # Simulate interruption detection (you can replace this with a more sophisticated logic)
        interruption_detected = input("Did you interrupt? (yes/no): ").lower() == "yes"
        if interruption_detected:
            conversation_handler.handle_interrupt()
