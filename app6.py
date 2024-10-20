import streamlit as st             # Module for building web apps
import speech_recognition as sr     # Module for speech recognition
import pyttsx3                      # Module for text-to-speech

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Streamlit app
st.title("Voice-to-Voice Chatbot")

st.write("Click the button below to start speaking.")

if st.button("Start Voice Input"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            st.write(f"You said: {user_input}")

            # Simple bot response logic
            response = f"You said '{user_input}'. This is a simple echo bot."
            st.write(f"Bot: {response}")

            # Speak the response
            speak(response)

        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.write(f"Could not request results from Google Speech Recognition service; {e}")
