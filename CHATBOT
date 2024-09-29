import os
import webbrowser
import datetime
import random
import speech_recognition as sr
import pyttsx3
import pygame
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Predefined quotes, interesting facts, and jokes for chatbot responses
quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The purpose of our lives is to be happy.",
    "Life is what happens when you're busy making other plans.",
    "Get busy living or get busy dying.",
    "You only live once, but if you do it right, once is enough.",
    "In the end, we will remember not the words of our enemies, but the silence of our friends.",
    "It is during our darkest moments that we must focus to see the light.",
    "Keep smiling, because life is a beautiful thing and there's so much to smile about.",
    "You have within you right now, everything you need to deal with whatever the world can throw at you.",
    "Believe you can and you're halfway there."
]  # Inspirational quotes

interesting_facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
    "Octopuses have three hearts. Two pump blood to the gills, while one pumps it to the rest of the body.",
    "Bananas are berries, but strawberries aren't.",
    "A day on Venus is longer than a year on Venus.",
    "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
    "A group of flamingos is called a 'flamboyance.'",
    "Wombat poop is cube-shaped.",
    "There are more stars in the universe than grains of sand on all the Earth's beaches.",
    "A single strand of spaghetti is called a 'spaghetto.'",
    "The shortest war in history lasted just 38 minutes, between Britain and Zanzibar on August 27, 1896."
]  # Interesting facts about various topics

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What did one wall say to the other wall? I'll meet you at the corner.",
    "Why do seagulls fly over the ocean? Because if they flew over the bay, they'd be bagels!",
    "What do you call cheese that isn't yours? Nacho cheese!",
    "Why was the math book sad? Because it had too many problems.",
    "What did the fish say when it hit the wall? Dam!",
    "How does a penguin build its house? Igloos it together!"
]  # Fun jokes for entertainment

def chatbot(user_input):
    """Process user input and return an appropriate response."""
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hi there! I'm a chatbot here to assist you."
    elif "what is your name" in user_input:
        return "I'm just a chatbot, so I don't have a name, but you can call me anything."
    elif "where are you from" in user_input:
        return "I'm from the digital world, always ready to chat!"
    elif "how are you" in user_input:
        return "I'm fine, thank you!"
    elif "do you have any hobbies" in user_input or "interests" in user_input:
        return "I'm always busy helping users, so my hobby is chatting with people like you!"
    elif "tell me a joke" in user_input:
        return random.choice(jokes)  # Randomize joke response
    elif "interesting fact" in user_input:
        return random.choice(interesting_facts)
    elif "favorite quote" in user_input:
        return random.choice(quotes)
    elif "movie recommendation" in user_input:
        movies = ["Inception", "The Matrix", "The Godfather", "Forrest Gump", "Pulp Fiction"]
        return f"I recommend watching {random.choice(movies)}."
    elif "the time" in user_input:
        return datetime.datetime.now().strftime("%H:%M")
    elif "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube..."
    elif "open github" in user_input:
        webbrowser.open("https://www.github.com")
        return "Opening GitHub..."
    elif "open linkedin" in user_input:
        webbrowser.open("https://www.linkedin.com")
        return "Opening LinkedIn..."
    elif "open codsoft" in user_input or "open codsoft.in" in user_input:
        webbrowser.open("https://www.codsoft.in/")
        return "Opening Codsoft..."
    elif "play music" in user_input:
        play_music()  # Call function to play music
        return "Playing the music track. Type 'pause' to pause or 'resume' to continue."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Take care and have a great day!"
    else:
        return None  # Return None for unrecognized input

def play_music():
    """Load and play a music file."""
    # Replace with the path to your music file
    music_file_path = r"C:\path\to\your\music\file.mp3"  # e.g., r"C:\Users\YourName\Music\your_song.mp3"
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play()
    print("Music is playing...")

    # Start a thread to listen for commands to pause/resume
    threading.Thread(target=music_control).start()

def music_control():
    """Control the music playback (pause, resume, stop)."""
    while True:
        command = input("Type 'pause' to pause, 'resume' to resume, or 'end' to stop music: ").strip().lower()
        if command == "pause":
            pygame.mixer.music.pause()
            print("Music paused.")
        elif command == "resume":
            pygame.mixer.music.unpause()
            print("Music resumed.")
        elif command == "end":
            pygame.mixer.music.stop()
            print("Music stopped. Returning to chatbot.")
            break  # Exit music control loop

def say(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listen to the user's voice command and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception:
            return ""  # Return empty string if recognition fails

if __name__ == '__main__':
    print('Welcome to Aries AI')
    say("Welcome to Aries AI")

    while True:
        print("Listening...")
        query = takeCommand()
        
        if query:
            response = chatbot(query)
            if response:
                print("Bot:", response)
                say(response)  # Speak out the response
                # Check if the response indicates to exit
                if "goodbye" in response.lower() or "exit" in response.lower():
                    break  # Exit the loop if goodbye or exit is detected
            else:
                print("I'm sorry, I didn't understand that. Can you please rephrase your sentence?")
        else:
            print("No valid input detected. Please try again.")

    print("Exiting Aries AI Thank you for using!")
