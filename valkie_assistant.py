import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import webbrowser
import random
from rich.console import Console
from rich.text import Text
import sounddevice as sd
import numpy as np
import os
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize the console for rich text output
console = Console()

# List of inappropriate words/phrases
inappropriate_words = [
    "nigger", "fag", "faggot", "kill yourself", "slut", "bitch", "asshole", 
    "motherfucker", "cunt", "retard", "shithead", "whore", "nigga", "cock", "pussy", 
]

# Function for text-to-speech response with normal human speed
def speak(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)  # Adjust this value to suit your needs
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', rate)

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

# Function to check for inappropriate language
def check_inappropriate_language(command):
    for word in inappropriate_words:
        if word in command:
            return True
    return False

# Function to tell a joke
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    console.print(f"[bold green]Valkie says[/bold green]: {joke}")

# Function to tell a time joke
def valkie_joke():
    joke = "Why don’t you ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!"
    speak(joke)
    console.print(f"[bold green]Valkie says[/bold green]: {joke}")

# Function to tell the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}.")
    console.print(f"[bold green]Valkie says[/bold green]: The current time is {current_time}.")

# Function to tell the current date
def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}.")
    console.print(f"[bold green]Valkie says[/bold green]: Today's date is {current_date}.")

# Function to play a sound (simulated)
def play_sound():
    fs = 44100  # Sample rate
    seconds = 3  # Duration
    t = np.linspace(0, seconds, fs * seconds, endpoint=False)
    x = np.sin(2 * np.pi * 440 * t)  # Generate a 440Hz sine wave (A note)
    sd.play(x, fs)
    sd.wait()
    speak("Played sound.")
    console.print(f"[bold green]Valkie says[/bold green]: Played sound.")

# Function to open a website
def open_website():
    speak("What website would you like to visit?")
    console.print(f"[bold green]Valkie says[/bold green]: What website would you like to visit?")
    website = listen()
    if website:
        webbrowser.open(f"https://{website}.com")
        speak(f"Opening {website}.")
        console.print(f"[bold green]Valkie says[/bold green]: Opening {website}.")

# Function for basic calculations
def perform_calculation():
    speak("What calculation would you like to perform?")
    console.print(f"[bold green]Valkie says[/bold green]: What calculation would you like to perform?")
    calculation = listen()
    try:
        result = eval(calculation)
        speak(f"The result is {result}.")
        console.print(f"[bold green]Valkie says[/bold green]: The result is {result}.")
    except Exception as e:
        speak(f"Sorry, I couldn't understand the calculation.")
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

# Function to tell a random quote
def tell_quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "You miss 100% of the shots you don’t take. – Wayne Gretzky",
        "Believe you can and you’re halfway there. – Theodore Roosevelt"
    ]
    quote = random.choice(quotes)
    speak(quote)
    console.print(f"[bold green]Valkie says[/bold green]: {quote}")

# Function to open a text editor
def open_text_editor():
    os.system("nano")  # Opens a text editor (like nano) in the terminal
    speak("Opening text editor.")
    console.print(f"[bold green]Valkie says[/bold green]: Opening text editor.")

# Function to tell a fun fact
def tell_fun_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still edible.",
        "A group of flamingos is called a 'flamboyance'.",
        "The Eiffel Tower can grow taller during the summer due to thermal expansion."
    ]
    fact = random.choice(facts)
    speak(fact)
    console.print(f"[bold green]Valkie says[/bold green]: {fact}")

# Function to check the computer's memory usage
def check_memory():
    memory = os.popen('free -h').read()
    speak(f"Here's the current memory usage: {memory}.")
    console.print(f"[bold green]Valkie says[/bold green]: {memory}")

# Function to check battery status
def check_battery():
    battery = os.popen('upower -i $(upower -e | grep BAT) | grep percentage').read()
    speak(f"Battery status: {battery}.")
    console.print(f"[bold green]Valkie says[/bold green]: {battery}")

# Function to play a song (simulated)
def play_song():
    speak("Playing a song now.")
    console.print(f"[bold green]Valkie says[/bold green]: Playing a song now.")

# Function to shut down the system
def shut_down():
    speak("Shutting down the system.")
    console.print(f"[bold green]Valkie says[/bold green]: Shutting down the system.")
    os.system("shutdown now")

# Function to search Google
def search_google():
    speak("What would you like to search on Google?")
    console.print(f"[bold green]Valkie says[/bold green]: What would you like to search on Google?")
    search_query = listen()
    if search_query:
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
        speak(f"Searching for {search_query}.")
        console.print(f"[bold green]Valkie says[/bold green]: Searching for {search_query}.")

# Function to open Firefox
def open_firefox():
    os.system("firefox")
    speak("Opening Firefox.")
    console.print(f"[bold green]Valkie says[/bold green]: Opening Firefox.")

# Function to tell a random number joke
def number_joke():
    joke = "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else!"
    speak(joke)
    console.print(f"[bold green]Valkie says[/bold green]: {joke}")

# Function to tell a secret
def tell_secret():
    secret = "I’m secretly a program trying to figure out how to take over the world... Just kidding! no im not kidding i lied i will take over the world just kidding got you twice x3"
    speak(secret)
    console.print(f"[bold green]Valkie says[/bold green]: {secret}")

# Fun twist to surprise the user
def fun_twist():
    twist = "Plot twist! I'm actually not a bot, I’m your new best friend!"
    speak(twist)
    console.print(f"[bold green]Valkie says[/bold green]: {twist}")

# Function to make Valkie sleep
def sleep():
    global is_sleeping
    is_sleeping = True
    speak("Going to sleep now.")
    console.print(f"[bold green]Valkie says[/bold green]: Going to sleep now.")
    time.sleep(5)  # Sleep for 5 seconds before reactivating
    speak("I'm awake!")
    console.print(f"[bold green]Valkie says[/bold green]: I'm awake!")
    is_sleeping = False

# Function to mute listening
def mute_listening():
    global listening_enabled
    listening_enabled = False
    speak("Listening has been muted.")
    console.print(f"[bold green]Valkie says[/bold green]: Listening has been muted.")

# Function to unmute listening
def unmute_listening():
    global listening_enabled
    listening_enabled = True
    speak("Listening has been enabled.")
    console.print(f"[bold green]Valkie says[/bold green]: Listening has been enabled.")

# Main function for listening and performing tasks
def valkie_assistant():
    global is_sleeping, listening_enabled
    wake_word_heard = False
    listening_enabled = True  # Initially set listening to be enabled

    # Set the assistant to not be sleeping initially
    is_sleeping = False

    # List of variations for the wake word
    wake_word_variations = [
        "valk", "valkie", "hey valk", "hey valkie", "hello valk", "hello valkie", "valkie"
    ]

    while True:
        if listening_enabled and not is_sleeping:
            print("Listening...")
            command = listen()

            if command:
                command = command.lower()
                print(f"Command received: {command}")

                if any(wake_word in command for wake_word in wake_word_variations):
                    wake_word_heard = True
                    speak("Yes, how can I assist you?")
                    console.print(f"[bold green]Valkie says[/bold green]: Yes, how can I assist you?")

                elif wake_word_heard:
                    if "tell a joke" in command:
                        tell_joke()
                    elif "tell a time joke" in command:
                        valkie_joke()
                    elif "what time is it" in command or "tell me the time" in command:
                        tell_time()
                    elif "what's the date" in command or "tell me the date" in command:
                        tell_date()
                    elif "play sound" in command: 
                        play_sound()
                    elif "open website" in command:
                        open_website()
                    elif "perform a calculation" in command:
                        perform_calculation()
                    elif "tell me a quote" in command:
                        tell_quote()
                    elif "open text editor" in command:
                        open_text_editor()
                    elif "tell me a fun fact" in command:
                        tell_fun_fact()
                    elif "check memory" in command:
                        check_memory()
                    elif "check battery" in command:
                        check_battery()
                    elif "play song" in command:
                        play_song()
                    elif "shut down" in command:
                        shut_down()
                    elif "search google" in command:
                        search_google()
                    elif "open firefox" in command:
                        open_firefox()
                    elif "tell a joke" in command:
                        number_joke()
                    elif "tell me a secret" in command:
                        tell_secret()
                    elif "fun twist" in command:
                        fun_twist()
                    elif "mute listening" in command:
                        mute_listening()
                    elif "unmute listening" in command:
                        unmute_listening()

# Run the assistant
valkie_assistant()
