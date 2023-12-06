import pyttsx3
import threading
import speech_recognition as sr
import nltk
from nltk.corpus import words
print('1')
# Download the words dataset for language detection
nltk.download('words')
print('2')
# Initialize the speech synthesis engine
engine = pyttsx3.init()
engine.setProperty('rate', 90)
print('3')
# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Flag to signal interruption
is_interrupted = False

# Set of English words for language detection
english_words = set(words.words())

def is_english_text(text):
    words_in_text = nltk.wordpunct_tokenize(text)
    return all(word.lower() in english_words for word in words_in_text)

def speak_thread(text):
    global is_interrupted
    with threading.Lock():
        engine.say(text)
        engine.runAndWait()
        is_interrupted = False  # Reset the interruption flag after speaking

def listen_user_input():
    global is_interrupted
    while True:
        with sr.Microphone() as source:
            print("Listening for user input...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            print("User said:", user_input)

            if is_english_text(user_input) and "stop" in user_input.lower():
                with threading.Lock():
                    is_interrupted = True

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio.")

def main():
    # Create a thread for speaking
    speak_text = "This is a test. Speaking slowly now."
    speak_thread_instance = threading.Thread(target=speak_thread, args=(speak_text,))

    # Create a thread for listening to user input
    listen_thread_instance = threading.Thread(target=listen_user_input)

    # Start both threads
    speak_thread_instance.start()
    listen_thread_instance.start()

    # Wait for both threads to finish
    speak_thread_instance.join()
    listen_thread_instance.join()

    print('done')

if __name__ == "__main__":
    main()
