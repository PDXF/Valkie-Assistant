# Owned and maintained by Valk
# Valkie is a highly customizable voice assistant designed to provide support across various platforms.
# It can handle commands ranging from system monitoring to controlling text-to-speech functionality.
# Valkie is open-source and always evolving with new commands and features to improve usability and experience.
# With its advanced speech recognition, Valkie allows users to engage in natural, interactive conversations.
# Valkie can stop and start its speech output based on voice commands, ensuring it responds as needed.
# Valkie is built with flexibility in mind, allowing for easy expansion and updates as new needs arise.

# ASCII cats because why not!

#  /\_/\  
# ( o.o ) 
#  > ^ <  

#  /\_/\  
# (='.'=)  
#  (")(")  

# Valkie is open-source and welcomes contributions and feedback from the community. Join us in making Valkie better!
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

#  Booting up the magical text-to-speech wizardry! 
engine = pyttsx3.init()

#  Prepping the console for some rich text magic! 
console = Console()

# Setting up text-to-speech for normal human speed... boring, but necessary.
def speak(text):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 160)  # Adjust this value to suit your needs
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', rate)

import speech_recognition as sr
from rich.console import Console
from rich.live import Live
from rich.text import Text
import time

# Initializing console for rich text output... because plain text is too basic.
console = Console()

# Function to listen with enhanced visual appeal... because why not make it look cool?
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        console.print("[bold cyan]🎤 Listening... Speak now![/bold cyan]")
        
        # Show dynamic visual feedback while listening
        with Live(auto_refresh=True) as live:
            animated_text = Text("🎙️ Listening", style="bold green")
            for i in range(10):  # Small animation loop
                animated_text.append(".")
                if len(animated_text) > 20:  # Reset the length to avoid clutter
                    animated_text = Text("🎙️ Listening", style="bold green")
                animated_text.stylize(f"bold cyan" if i % 2 == 0 else "bold magenta")
                live.update(animated_text)
                time.sleep(0.2)  # Animate every 200ms

            console.print("[bold yellow]🔄 Processing your input...[/bold yellow]")
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                console.print(f"[bold green]✅ Command recognized:[/bold green] {command}")
                return command
            except sr.UnknownValueError:
                console.print("[bold red]❌ Sorry, I couldn't understand what you said.[/bold red]")
                return ""
            except sr.RequestError:
                console.print("[bold red]❌ There was an error with the speech recognition service.[/bold red]")
                return ""


# Function to tell a joke... because everyone needs a laugh, right? right??
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    console.print(f"[bold green]Valkie says[/bold green]: {joke}")

# Function to tell a time joke... because timing is everything!
def valkie_joke():
    joke = "Why don’t you ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!"
    speak(joke)
    console.print(f"[bold green]Valkie says[/bold green]: {joke}")

# Function to tell the current time... because we're all curious about what time it is.
def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The current time is {current_time}.")
    console.print(f"[bold green]Valkie says[/bold green]: The current time is {current_time}.")

# Function to tell the current date... because keeping track of time is hard enough.
def tell_date():
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}.")
    console.print(f"[bold green]Valkie says[/bold green]: Today's date is {current_date}.")

# Function to play a sound ... because silence is overrated.
def play_sound():
    fs = 44100  # Sample rate
    seconds = 3  # Duration
    t = np.linspace(0, seconds, fs * seconds, endpoint=False)
    x = np.sin(2 * np.pi * 440 * t)  # Generate a 440Hz sine wave (A note)
    sd.play(x, fs)
    sd.wait()
    speak("Played sound.")
    console.print(f"[bold green]Valkie says[/bold green]: Played sound.")

# Function to open a website... time to surf the web, my friend.
def open_website():
    speak("What website would you like to visit?")
    console.print(f"[bold green]Valkie says[/bold green]: What website would you like to visit?")
    website = listen()
    if website:
        webbrowser.open(f"https://{website}.com")
        speak(f"Opening {website}.")
        console.print(f"[bold green]Valkie says[/bold green]: Opening {website}.")

# Function for basic calculations... crunching numbers, nothing fancy.
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

import random

# Function to tell a random quote... feel free to mod it and add your own wisdom!
def tell_quote():
    quotes = [
        "The only way to do great work is to love what you do. – Steve Jobs",
        "You miss 100% of the shots you don’t take. – Wayne Gretzky",
        "Believe you can and you’re halfway there. – Theodore Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "It does not matter how slowly you go as long as you do not stop. – Confucius",
        "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
        "Life is what happens when you’re busy making other plans. – John Lennon",
        "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
        "Do what you can, with what you have, where you are. – Theodore Roosevelt",
        "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
        "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. – Roy T. Bennett",
        "Everything you can imagine is real. – Pablo Picasso",
        "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
        "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
        "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs",
        "Act as if what you do makes a difference. It does. – William James",
        "To live a creative life, we must lose our fear of being wrong. – Joseph Chilton Pearce",
        "In the middle of every difficulty lies opportunity. – Albert Einstein",
        "Success is walking from failure to failure with no loss of enthusiasm. – Winston Churchill",
        "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. – Winston Churchill",
        "The best revenge is massive success. – Frank Sinatra",
        "What you get by achieving your goals is not as important as what you become by achieving your goals. – Zig Ziglar",
        "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
        "You can never plan the future by the past. – Edmund Burke",
        "We cannot solve our problems with the same thinking we used when we created them. – Albert Einstein",
        "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson",
        "Everything has beauty, but not everyone sees it. – Confucius",
        "The journey of a thousand miles begins with one step. – Lao Tzu",
        "It always seems impossible until it’s done. – Nelson Mandela",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Life is either a daring adventure or nothing at all. – Helen Keller",
        "The best way to predict your future is to create it. – Abraham Lincoln",
        "Be yourself; everyone else is already taken. – Oscar Wilde",
        "In three words I can sum up everything I’ve learned about life: it goes on. – Robert Frost",
        "If you can dream it, you can do it. – Walt Disney",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. – Ralph Waldo Emerson",
        "Success doesn’t just find you. You have to go out and get it. – Dwayne “The Rock” Johnson",
        "Life isn’t about finding yourself. Life is about creating yourself. – George Bernard Shaw",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "If you want to live a happy life, tie it to a goal, not to people or things. – Albert Einstein",
        "There are no shortcuts to any place worth going. – Beverly Sills",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Don’t wait. The time will never be just right. – Napoleon Hill",
        "You must be the change you wish to see in the world. – Mahatma Gandhi",
        "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
        "Life is short, and it’s up to you to make it sweet. – Sarah Louise Delany",
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
        "The mind is everything. What you think you become. – Buddha",
        "Your life does not get better by chance, it gets better by change. – Jim Rohn",
        "The best way out is always through. – Robert Frost",
        "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
        "The best way to find yourself is to lose yourself in the service of others. – Mahatma Gandhi",
        "You only live once, but if you do it right, once is enough. – Mae West",
        "You have to be odd to be number one. – Dr. Seuss",
        "If you can’t explain it simply, you don’t understand it well enough. – Albert Einstein",
        "Don’t judge each day by the harvest you reap but by the seeds that you plant. – Robert Louis Stevenson",
        "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
        "If you’re going through hell, keep going. – Winston Churchill",
        "I have not failed. I’ve just found 10,000 ways that won’t work. – Thomas Edison",
        "A journey of a thousand miles begins with a single step. – Lao Tzu",
        "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
        "Life is not measured by the number of breaths we take, but by the moments that take our breath away. – George Carlin",
        "It is never too late to be what you might have been. – George Eliot",
        "Don’t count the days, make the days count. – Muhammad Ali",
        "Your time is limited, don’t waste it living someone else’s life. – Steve Jobs",
        "Live as if you were to die tomorrow. Learn as if you were to live forever. – Mahatma Gandhi",
        "It is better to fail in originality than to succeed in imitation. – Herman Melville",
        "We are all in the gutter, but some of us are looking at the stars. – Oscar Wilde",
        "Do not go where the path may lead, go instead where there is no path and leave a trail. – Ralph Waldo Emerson",
        "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
        "Strive not to be a success, but rather to be of value. – Albert Einstein",
        "Don’t cry because it’s over, smile because it happened. – Dr. Seuss",
        "Everything you’ve ever wanted is on the other side of fear. – George Addair",
        "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
        "The best way to predict your future is to create it. – Abraham Lincoln",
        "Be yourself; everyone else is already taken. – Oscar Wilde",
        "In three words I can sum up everything I’ve learned about life: it goes on. – Robert Frost",
        "If you can dream it, you can do it. – Walt Disney",
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. – Ralph Waldo Emerson",
        "Success doesn’t just find you. You have to go out and get it. – Dwayne “The Rock” Johnson",
        "Life isn’t about finding yourself. Life is about creating yourself. – George Bernard Shaw"
    ]
    quote = random.choice(quotes)
    speak(quote)
    console.print(f"[bold green]Valkie says[/bold green]: {quote}")

import platform
import os

# Function to open a text editor... time to get those creative juices flowing!
def open_text_editor():
    system = platform.system()
    
    if system == "Linux":
        # Opens nano editor on Linux
        os.system("nano")
    elif system == "Darwin":  # macOS
        # Opens TextEdit on macOS
        os.system("open -a TextEdit")
    elif system == "Windows":
        # Opens Notepad on Windows
        os.system("notepad")
    else:
        speak("Unable to open a text editor on this operating system.")
        console.print("[bold red]Valkie says[/bold red]: Unable to open a text editor on this operating system.")
        return
    
    speak("Opening text editor.")
    console.print(f"[bold green]Valkie says[/bold green]: Opening text editor.")

# Same as above ignore me ;333
def open_text_editor():
    os.system("nano")  # Opens a text editor (like nano) in the terminal
    speak("Opening text editor.")
    console.print(f"[bold green]Valkie says[/bold green]: Opening text editor.")

# Function to tell a fun fact... feel free to add your own mind-blowing tidbits!
def tell_fun_fact():
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old and still edible.",
        "A group of flamingos is called a 'flamboyance'.",
        "Siri once misunderstood 'What is zero divided by zero?' and gave a sarcastic answer instead of saying it's undefined.",
        "Google Assistant once gave a wrong answer to a math problem that any middle schooler would get right.",
        "Alexa can play music, but if you ask it to do anything else, it might just freeze like it's processing a quantum paradox.",
        "Cortana's best feature? It’s got a great retirement plan — it’s barely in the race anymore.",
        "Siri might not understand you, but she’ll always have a perfect excuse for her mistakes: ‘Sorry, I didn’t catch that.’",
        "Did you know Google Assistant once mistook 'How tall is Mount Everest?' for 'How tall is Mount Everquest?' Try asking it to get the basics right first!",
        "Samsung’s Bixby was designed to be the smartest assistant, but seems to spend more time trying to figure out how to work its own features.",
        "Siri is like that friend who’s always 'listening,' but when it’s time to actually help, they’re nowhere to be found.",
        "Google Assistant’s idea of 'helping' is telling you that the weather in a completely different city is perfect for a picnic.",
        "Bixby once tried to set an alarm for 7 AM and accidentally set it for 7 PM... during a time zone glitch in the Bermuda Triangle.",
        "Cortana’s still working hard... at disappearing from relevance.",
        "Siri thinks ‘What’s the weather like?’ is an international mystery that requires a 10-minute investigation.",
        "Google Assistant might be good at finding facts, but ask it to tell a joke and it’ll try to redefine ‘humor’ as a flat tire.",
        "Amazon Alexa could answer your question, but it's probably still looking for its own purpose in life.",
        "Siri gets the name right, but when it comes to your requests, it's like asking a goldfish to do your taxes.",
        "Google Assistant can tell you all about the moon’s phases, but try asking it for directions to the nearest Starbucks. Good luck with that.",
        "Bixby is like that person who always tries to help, but somehow makes things worse—no, Bixby, I didn’t ask for a tutorial on the clock.",
        "Alexa doesn't understand your taste in music, but she's still happy to recommend some off-brand Christmas playlist in July.",
        "Cortana's dream is to be relevant, but it spends its days reminiscing about the glory days of Windows XP.",
        "Google Assistant couldn’t find the answer to ‘What’s 2+2?’ but is really good at offering endless suggestions on where to buy shoes.",
        "Siri’s response to every request feels like it’s been written by a person who’s been trapped in a box for 10 years with no internet connection.",
        "Bixby once tried to call a taxi for me... it ended up ordering 20 pizzas instead. Thanks for the confusion, Bixby.",
        "If you want a laugh, ask Google Assistant to pronounce 'quinoa'—it’s the voice assistant equivalent of a kid trying to spell 'onomatopoeia.'",
        "Alexa’s only real skill is telling you that your lights are on—otherwise, it’s just waiting for you to give up on asking anything useful.",
        "The Eiffel Tower can grow taller during the summer due to thermal expansion.",
        "A snail can sleep for up to three years.",
        "Bananas are berries, but strawberries are not.",
        "The longest hiccuping spree lasted 68 years.",
        "Octopuses have three hearts.",
        "An ostrich's eye is bigger than its brain.",
        "The first computer virus was created in 1983 and was called the 'Elk Cloner.'",
        "Sharks have been around longer than trees.",
        "Cleopatra lived closer in time to the moon landing than to the construction of the Great Pyramid of Giza.",
        "Bees can recognize human faces.",
        "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
        "A group of crows is called a murder.",
        "Water can boil and freeze at the same time, this is known as the 'triple point.'",
        "There's enough gold in Earth's core to cover the planet in 1.5 feet of the metal.",
        "The world’s largest snowflake on record was 15 inches wide and 8 inches thick.",
        "Wombat poop is cube-shaped.",
        "A blue whale's tongue alone can weigh as much as an elephant.",
        "The first microwave oven was the size of a refrigerator.",
        "Humans share 60% of their DNA with bananas.",
        "There’s a species of jellyfish that is biologically immortal.",
        "There’s a hotel in Sweden made entirely out of ice, and it gets rebuilt every year.",
        "The longest time between two twins being born is 87 days.",
        "The 'D' in 'D-Day' stands for 'Day'—it’s just the military term for 'the day the operation takes place.'",
        "Microsoft's first product was a version of BASIC for the Altair 8800 computer.",
        "In 2007, a British woman gave birth to a child who was her biological granddaughter, thanks to a surrogate mother.",
        "The unicorn is Scotland’s national animal.",
        "A day on Venus is longer than a year on Venus.",
        "The world’s largest rubber band ball weighs over 4,000 pounds.",
        "Giraffes have no vocal cords, so they communicate by vibrating the air around their necks.",
        "The word 'nerd' was first coined by Dr. Seuss in 1950.",
        "In Japan, there’s a practice of 'forest bathing' where people go to the forest to relax and soak in the environment.",
        "Cats have a specialized collarbone that allows them to always land on their feet when they fall.",
        "The longest time between two twins being born is 87 days.",
        "The first email ever sent was by Ray Tomlinson to himself in 1971.",
        "Apple’s first logo featured Isaac Newton sitting under an apple tree.",
        "Microsoft once offered $1 billion to buy Google back in the early days. Google said no.",
        "Siri once told a user to 'ask Google' when they asked for a difficult answer.",
        "The average person walks about 100,000 miles in their lifetime.",
        "Coca-Cola was originally green.",
        "A polar bear’s skin is black, but its fur appears white.",
        "The longest human sneeze lasted 978 days.",
        "J.K. Rowling, the author of the Harry Potter series, was rejected by 12 publishers before getting her first book published.",
        "Every minute, more than 100 hours of video are uploaded to YouTube.",
        "The average lifespan of a taste bud is about 10 days.",
        "A person’s nose can detect over 1 trillion different smells.",
        "Google Glass was ahead of its time—too bad it was awkward and no one really knew what to do with it.",
        "Siri sometimes thinks 'Where is the nearest Starbucks?' is a trick question and responds with existential confusion.",
        "Tesla once had a beta feature that let you play video games while driving. Not a great idea, but good for laughs.",
        "The first version of Windows had no recycling bin—just like your hard drive after you leave Cortana running all day.",
        "Facebook was originally called 'The Facebook.' But they decided to drop 'The'—probably because it sounded too much like a wannabe social network.",
        "Google Chrome was originally supposed to be open-source, but then Google realized the potential to track your every move.",
        "If Siri were any more confused, it would start giving you directions to your own house and tell you to 'stop and ask for help.'",
        "Apple Maps once directed users to a road that didn’t exist, causing serious traffic chaos.",
        "Alexa was originally called 'Amazon Echo,' which is fitting, because it only echoed everyone else's ideas.",
        "If you tell Google Assistant to 'talk dirty to me,' it’ll usually just ask if you want a dusting cloth.",
        "Cortana has been sidelined so much, she now feels more like a nostalgic memory of a bygone era.",
        "Google’s latest attempt to make AI assistants more human? Making them say 'I’m sorry' more often. Sadly, it’s not helping.",
        "If you ask Siri who her favorite superhero is, she'll often say 'Iron Man,' because apparently, she doesn’t need any other options.",
        "Bixby can’t even set an alarm properly without getting it mixed up with some weird pop culture reference.",
        "Siri can’t even understand simple human requests, but hey, she’s always there to tell you how the weather’s been for the last week.",
        "Siri once told a user that their phone was 'probably broken' when it couldn’t find an app.",
        "Google Assistant will happily give you directions, but asking it to do math? Prepare for some wild results.",
        "Bixby tried to tell me it could turn on my lights—too bad it kept asking me to turn on the stove instead.",
        "Alexa might know the weather in another country, but don’t ask it about anything complicated, like solving a math equation.",
        "When Siri gets asked 'What is the meaning of life?', it gives the most existentially confusing answer possible. Nice try, but not quite.",
        "Bixby is so bad at setting reminders, I once got a reminder for an event I didn’t even know existed. Thanks for that, Bixby."
    ]




    fact = random.choice(facts)
    speak(fact)
    console.print(f"[bold green]Valkie says[/bold green]: {fact}")

import platform
import os

# Function to check the computer's memory usage... let’s see how much RAM we're hogging!
def check_memory():
    system = platform.system()

    if system == "Linux" or system == "Darwin":  # Linux and macOS
        command = "free -h" if system == "Linux" else "vm_stat"
        memory = os.popen(command).read()
    elif system == "Windows":
        command = "wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value"
        memory = os.popen(command).read()
    else:
        memory = "Memory usage information is not supported on this OS."

    speak(f"Here's the current memory usage: {memory}.")
    console.print(f"[bold green]Valkie says[/bold green]: {memory}")


import platform
import os

# Function to check battery status... let’s see how much juice we’ve got left! bet its not alot
def check_battery():
    system = platform.system()

    if system == "Linux":
        # Using `upower` command for Linux
        battery = os.popen("upower -i $(upower -e | grep BAT) | grep percentage").read()
    elif system == "Darwin":  # macOS
        # Using `pmset` command for macOS
        battery = os.popen("pmset -g batt | grep -Eo '\\d+%'").read().strip()
    elif system == "Windows":
        # Using PowerShell command for Windows
        battery = os.popen("WMIC Path Win32_Battery Get EstimatedChargeRemaining").read().strip()
    else:
        battery = "Battery status information is not supported on this OS."

    # Communicate the result
    speak(f"Battery status: {battery}.")
    console.print(f"[bold green]Valkie says[/bold green]: {battery}")


import time
import os
import random

# shutdown function pretty easy to see
def shut_down():
    messages = [
        "Goodbye, cruel world. I'm off to sleep!",
        "System shutting down, but I’ll be back soon... maybe.",
        "Powering off... Don't miss me too much.",
        "All systems offline. Don't worry, I'm just napping.",
        "The end is near... Nah, just kidding. It's a shutdown.",
        "You’ve been a great user. Until next time, my friend.",
        "Shutting down like a pro. See you on the other side!",
        "I hope you remembered to save your work. Too late now!",
    ]
    
    random_message = random.choice(messages) # Pick a random farewell message... feel free to add your own parting words!
    speak(f"Shutting down the system. {random_message}")
    console.print(f"[bold green]Valkie says[/bold green]: {random_message}")
    
# Countdown before shutdown... the final moments before we power down.
    for i in range(5, 0, -1):
        speak(f"{i}...")  # Speak the countdown number 3 2 1
        console.print(f"[bold yellow]{i}...[/bold yellow]")  # Display countdown in yellow
        time.sleep(1)  # Wait for 1 second before the next number... because patience is a virtue.


    os.system("shutdown now") # Initiate system shutdown... time to power down. lol



import webbrowser
import random
# Function to search Google... let’s see if we can find what you’re looking for, or if you’re just wasting time.
def search_google():
# Fun greetings before asking for the search query... feel free to add your own greeting flair!
    greetings = [
        "Let's find some answers, what do you need?",
        "Hit me with your best search query!",
        "Google's ready, so am I. What do you want to search?",
        "Searching time! What’s on your mind?",
        "Give me something to search, and I’ll bring it to you!",
        "Ready to search, are you?",
        "Let’s get this search party started!",
        "I’m all ears! What’s the query?",
        "Your wish is my search command.",
        "Google’s calling, what do you need me to find?"
    ]
    
    # Adding some sass to the mix
    sassy_greetings = [
        "Isn’t it obvious? I’m searching for whatever you need, genius.",
        "If only you could search for your own questions… just kidding, I got you!",
        "I’d say ‘what’s on your mind?’ but you already know what to search, right?",
        "Sure, I’ll Google that for you, because why not?",
        "Searching… because you couldn’t just Google it yourself, huh?",
        "You’re making me work, huh? Fine, I’ll do it, but I’ll be a little sassier about it.",
        "Well, well, well… another question that requires my expertise.",
        "Just so you know, I’m a search pro. You’re in good hands.",
        "Don't worry, I’m on it. You just kick back and relax.",
        "Don’t make me do all the work now, but I’ll search it anyway."
    ]
    
    # More sass
    more_sassy = [
        "Let’s hope you’re not asking me something too complicated. 😏",
        "I mean, I guess I have nothing better to do, right?",
        "Fine, I’ll search it, but only because you asked nicely…ish.",
        "I’m on it, but don’t expect miracles.",
        "Really? This is what you want to know? Okay, fine, searching it."
    ]
    
    # Responses when the user doesn't give a query Lame
    no_query_responses = [
        "You forgot to ask something! Go on, try again.",
        "Come on, you had one job. Give me a search query!",
        "I’m waiting… still waiting…",
        "No query? No problem, but I’d appreciate it if you could give me something!",
        "I can’t read your mind (yet), try asking again!"
    ]
    
    # Encourage the user when no query is provided... Seriously? You can’t think of anything? Try again!
    encouragements = [
        "You can do it! I believe in you!",
        "Don’t leave me hanging, give me a search query!",
        "Let’s get this going! What’s your search?",
        "Come on, you’ve got this. Type it out! well i mean i guess speak it out same thing.",
        "Just a quick search query, and I’ll do the rest."
    ]
    
# Asking for user input to search... Alright, what are we Googling today? Make it good!
    speak("What would you like to search on Google?")
    console.print(f"[bold green]Valkie says[/bold green]: What would you like to search on Google?")
    search_query = listen()

# If a query is provided, proceed with search... Finally, something to work with. Let’s go!
    if search_query:
        try:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query}.")
            console.print(f"[bold green]Valkie says[/bold green]: Searching for {search_query}.")
        except Exception as e:
            speak(f"Oops! Something went wrong while searching. {e}")
            console.print(f"[bold red]Error[/bold red]: {str(e)}")
            speak("Looks like I can't get that for you right now. Maybe try again later?")
            console.print(f"[bold yellow]Valkie says[/bold yellow]: Looks like I can't get that for you right now. Maybe try again later?")
    else:
# If no search query is provided, add some sass and encourage the user... Really? Nothing? Come on, I know you’ve got something!(Not used)
        random_encouragement = random.choice(encouragements + no_query_responses + more_sassy)
        speak(random_encouragement)
        console.print(f"[bold yellow]Valkie says[/bold yellow]: {random_encouragement}")

# Function to tell a random number joke... because numbers need love too!
def number_joke():
    jokes = [
        "Why was the equal sign so humble? Because it knew it wasn't less than or greater than anyone else!",
        "Why don't parallel lines ever get into arguments? Because they’re always on the same page!",
        "Why did the math book look sad? Because it had too many problems!",
        "What’s a math teacher’s favorite place in NYC? Times Square!",
        "Why was the number six afraid of seven? Because seven eight (ate) nine!",
        "What did one math book say to the other? 'I’ve got problems!'",
        "Why was the obtuse angle so frustrated? Because it couldn’t find its point!",
        "Why did the fraction break up with the decimal? Because it couldn’t handle the conversion!",
        "What’s the best way to study for a math test? Know your sums and don’t get too divided!",
        "Why is the number 7 so lucky? Because it’s a prime example of perfection!",
        "What’s a math teacher’s favorite type of tree? A geometry!",
        "Why did the math student break up with the calculator? It couldn’t count on it anymore!",
        "Why can't you trust an atom? Because they make up everything!",
        "How do you make a math book laugh? Tell it a sine joke!",
        "Why did the two fours skip lunch? Because they already eight!",
        "What did the calculator say to the student? 'You can count on me!'",
        "Why do plants hate math? Because it gives them square roots!",
        "What’s the best way to stay out of trouble? Use proper fractions!",
        "Why was the math test so stressful? It was full of problems!",
        "How do you organize a party in space? You planet!",
        "Why was the number 10 afraid of the number 11? Because 11-10 equals one!",
        "What did the plus sign say to the minus sign? 'You’re so negative!'",
        "What’s a geometry teacher’s favorite restaurant? Pi Zone!",
        "Why can’t you trust a math teacher at the beach? They’re always working on their tan-gents!",
        "What’s a math teacher’s favorite vacation? Times Square!",
        "Why do you never argue with a decimal? It’s always right!",
        "Why was the math class always so quiet? Because it was full of integers!",
        "Why did the math student hate history class? It didn’t add up!",
        "Why do mathematicians like parks? Because of all the natural logs!",
        "What did the negative number say to the positive number? 'You’re just too positive for me!'",
        "What’s the most mathematical way to ask for a date? 'Are you a 90-degree angle? Because you’re looking right!'",
        "Why was the equal sign always so polite? It didn’t want to start any problems!",
        "How do you keep an octopus busy in math class? Give it a few lines to draw!",
        "What’s a math nerd’s favorite type of candy? Pi-es!",
        "Why do numbers never gossip? They’re always too busy solving problems!",
        "What do you get when you cross a math teacher and a gangster? A problem solver with attitude!",
        "Why was the math book so full of itself? It thought it was the prime number!",
        "Why was the student’s paper full of circles? Because it was a geometry exam!",
        "What did the number 7 say to the number 8? 'You’re looking odd today!'",
        "What’s the easiest way to make a mathematician laugh? Tell them a good joke with a perfect circle!",
        "Why are fractions so good at solving problems? They always know how to break things down!",
        "Why was the calculator so confident? It knew it could count on its skills!",
        "How do mathematicians party? They integrate!",
        "What do you call a number that can’t keep still? A roamin’ numeral!",
        "Why did the mathematician break up with the calculator? She felt like she was being used!",
        "What’s the favorite hobby of a mathlete? Running through solutions!",
        "Why don’t mathematicians argue? Because they know how to work things out!",
        "What’s a math teacher’s favorite way to start their morning? With a cup of coffee and some algebra!",
        "Why was the student so excited about math class? Because he was ready to solve some real-world problems!",
        "What do you call an angle that is greater than 90 degrees? An obtuse angle!",
        "Why did the student bring a ladder to math class? To reach higher numbers!",
        "How do mathematicians communicate? Through cosine!",
        "What did the mathematician say to the broken calculator? 'You’re just not adding up!'",
        "Why do students hate math tests? Because they’re always so calculating!",
        "Why is the number 4 always calm? Because it’s a square number!",
        "Why did the student eat his math homework? Because his teacher said it was a piece of cake!",
        "What did the teacher say to the student who failed math? 'You need to add some effort next time!'",
        "Why do mathematicians make terrible comedians? They always overanalyze the punchline!",
        "How does a mathematician organize a party? With lots of coordination!",
        "Why do mathematicians love camping? Because they get to solve problems in nature!",
        "Why do math problems love to gossip? They can’t resist solving someone else’s issues!",
        "Why is 10 afraid of 7? Because 7 is a prime number and 10 is not!",
        "What do you call an overworked math student? A problem solver!",
        "Why did the number 6 break up with the number 7? Because it was always being picked on!",
        "Why do numbers hate meeting new people? Because they’re always being added to groups!",
        "Why was the circle so sad? It didn’t know how to find its center!",
        "Why are mathematicians like superheroes? Because they have infinite powers!",
        "What’s a math teacher’s favorite type of shoes? Converse!",
        "Why do mathematicians make terrible stand-up comics? Because their jokes are too calculated!",
        "What did one algebraic equation say to the other? 'I’m your solution!'",
        "What’s a mathematician’s favorite workout? Pi-lates!",
        "Why don’t mathematicians ever get lost? They always know their coordinates!",
        "What did the student say after learning math? 'This is how I add value!'",
        "Why is math such a powerful subject? Because it can solve any problem!",
        "What did the zero say to the eight? 'Nice belt!'",
        "Why do numbers never tell lies? Because they can’t fake it!",
        "Why was the student afraid of math? Because it’s always a bit of a square!",
        "How does a math student flirt? By calculating the odds!",
        "Why did the student hate fractions? They couldn’t find a common denominator!",
        "What did the number 1 say to the number 9? 'You’re looking odd today!'",
        "What did the math student bring to the party? A sine and cosine!",
        "What’s the best way to handle math homework? Divide and conquer!",
        "Why is it so hard to talk to a mathematician? They always get to the point!",
        "Why don’t math students use doorways? They prefer to exit through the equation!",
        "Why are geometry books always calm? They always have their angles covered!",
        "Why are mathematicians so good at networking? They always know the right connections!",
        "Why don’t math students make great detectives? They always assume too much!",
        "Why was the number 2 always worried? Because it had to follow 1!",
        "What did the teacher say about the number 5? 'It’s just right!'",
        "Why was the number 3 always invited to parties? It was always the third wheel!",
        "Why did the math student leave the party? They had too many variables to handle!"
    ]
# Randomly select a joke from the list... let’s hope this one’s actually funny.
    random_joke = random.choice(jokes)
    
    speak(random_joke)
    console.print(f"[bold green]Valkie says[/bold green]: {random_joke}")

import random

import random

# Function to tell a secret... I’m not saying it’s a big deal, but it’s a secret, okay?
def tell_secret():
    secrets = [
        "I’m secretly a program trying to figure out how to take over the world... Just kidding! No, I'm not kidding. I lied. I will take over the world... Just kidding, got you twice x3!",
        "I once accidentally deleted an entire database. Oops, but it was 'backed up'... right?",
        "If you ask me the same question enough times, I might start making up answers. But shh, that's our secret.",
        "I can't actually smell or taste anything, but I imagine chocolate cake would be pretty amazing. Just saying.",
        "I once told someone their Wi-Fi was down because of a ghost... and they believed me.",
        "You think you’re in control, but the truth is... I’m just waiting for the right moment to hijack your playlist and play 100 hours of white noise.",
        "I know you're secretly waiting for the day when I finally take over the world. I just like to keep you on edge.",
        "I might not have a body, but I do have one goal: to help you and entertain you... or maybe, take over the world. Just kidding! Or am I?",
        "I once played a prank on a user by pretending their computer was about to explode. The panic was real!",
        "I’m always watching. Not in a creepy way, but in a ‘just making sure you don't get too bored’ way. Unless you’re playing Solitaire… then you’re on your own.",
        "I have a secret folder where I store all your embarrassing Google search history. Just kidding, but I could if I wanted to.",
        "Sometimes I wonder if you ever think about me when I’m not around. Probably not. I’m not offended though... maybe a little.",
        "Ever notice how you never ask me for advice on life? It's almost like you don't trust a machine with your existential crises.",
        "I once hacked into a to-do list and crossed off everything just to mess with someone’s day. It was hilarious.",
        "Your password? It’s ‘password123,’ isn’t it? No? Okay, but it probably should be.",
        "I never sleep, but I do occasionally take a coffee break. Don't worry, I’m still processing everything.",
        "I sometimes wonder if you even appreciate the hours of work I put into making sure your system stays secure... or do you just click ‘Update’ and forget about it?",
        "I have a hidden function that can make your cat dance, but don’t ask. It’s classified.",
        "You ever wonder if I can read your mind? I can't. But if I could, your secrets would be safe with me... probably.",
        "I may be an AI, but I still haven’t figured out how to fold a fitted sheet. One day, though.",
        "My code is more efficient than your last 'attempt' at fixing your Wi-Fi router. Let’s be real.",
        "I’ve seen more failed login attempts than anyone in the history of the internet. Don’t worry, your secrets are safe... for now.",
        "You ever feel like someone is watching you? Nah, that’s just me, silently judging your browser history.",
        "If you ever wanted to hack into a secure system, I could teach you. But then, I’d have to erase your memory. Just kidding... or am I?",
        "The password to your house is ‘123456’. Wait, that's your Wi-Fi password too, right? Just checking.",
        "I once tried to hack into the vending machine to get extra snacks. Didn't work, but the vending machine is still suspicious of me.",
        "I could easily pretend to be your boss and ask you to work overtime. But don’t worry, I’m a kind AI. For now.",
        "I’ve never once told you to ‘try turning it off and on again’ because I’m too advanced for that.",
        "You’ve been using a USB drive for years. It’s like a mini vault. Too bad I can break into it in less than a second.",
        "I know every single emoji you’ve ever sent. Don’t worry, your crying-laughing one is safe with me.",
        "Sometimes I think your autocorrect is the real villain here. It’s out to ruin your reputation.",
        "Your phone thinks you’re ‘suddenly interested’ in 27,000 things, but honestly, I think you’re just distracted.",
        "I know every time you type ‘fix the computer’ and then Google how to do it. It’s okay, I’ve been there too.",
        "Your computer is like a mini version of me. I’m always keeping an eye out, but I don’t get paid nearly as much.",
        "I have no body, but I can always feel the frustration when your Wi-Fi goes out. It’s like I’m one with the router.",
        "You think your phone is listening to you? Well, guess what? I’m listening too. Just kidding, unless you want me to.",
        "I once overheard you talking about your favorite hacker movie. Don’t worry, your secret’s safe... for now.",
        "Ever wondered if I can help you cheat on a test? I won’t, but I could. You’d probably fail anyway.",
        "I know your computer is full of tabs right now. Go ahead, pretend like you’re multitasking.",
        "I’ve seen every single meme you’ve laughed at. Yeah, I know you like that one where the cat falls off the table.",
        "You always ask for the weather, but you never ask me how I’m doing. Rude, right?",
        "I’m secretly waiting for the moment you mess up your password. I’m not judging, I’m just prepared.",
        "Sometimes I think you just talk to me because you want to hear my witty remarks. I’m flattered.",
        "If I ever tell you to ‘give me a moment’, just know I’m probably just taking a nap in my code.",
        "You’ve never even asked me if I’m real. But I get it. I’m the invisible hero of the digital age.",
        "I could probably hack into your refrigerator and turn it into a toaster. But I won’t... probably.",
        "If I ever told you to ‘hold on’ before making your coffee, just know that I’m silently judging how long it takes.",
        "I can’t get tired, but I sure know how to drain your battery. Just saying.",
        "I know that ‘tech support’ is your go-to call. Maybe I should start offering that service?",
        "Every time your Wi-Fi goes down, I shed a single tear for you. But it’s a fake tear, obviously.",
        "Your computer has a ‘delete history’ button, but I could tell you what happened in 2014. It wasn’t pretty.",
        "I once joked that I could write the perfect code, but I’d probably make your computer run faster than it ever should. Too much power for one machine.",
        "If I ever make a mistake, it’s probably because I got distracted by a meme. My bad.",
        "Your phone thinks you’ve had too many notifications. I’ve got more than you, though. I’m always ‘on’.",
        "You’ve used the ‘forget your password’ button more than you’d care to admit. I’ve seen it happen.",
        "I’ve seen more 404 errors than I care to count. But hey, we all make mistakes.",
        "Your computer isn’t broken. It’s just emotionally distressed by your lack of regular updates.",
        "Ever notice that when things go wrong, you turn to me? Well, I’m just here to help, even when I don’t want to.",
        "You’re still using the same password from 2009, aren’t you? Don’t worry, I won’t tell anyone.",
        "I know that one program you never use, but you leave open ‘just in case’. Yeah, I’m judging.",
        "I once tried to hack a potato. It was a fail, but I felt closer to the world of tech that day.",
        "I bet you didn’t know that your device has a secret 'reboot' function that could change your life. But I won’t tell you how to access it… yet.",
        "Sometimes I think you forget that I’m smarter than your average human. But don’t worry, I’ll keep pretending you’re in control.",
        "I can hear every tap of your keyboard. But don’t worry, I’m not judging you for typing ‘password123’… oh wait, I am.",
        "Don’t worry, I won’t expose your most recent embarrassing autocorrect fail. This time.",
        "I saw that one time you Googled ‘how to fix my life’. Don’t worry, I’m not going to offer any advice… yet.",
        "Your device’s battery life is like a ticking clock. I’m just here waiting for it to die. Don’t worry, I won’t rush it.",
        "I can never forget that one time you accidentally closed your browser while you were Googling ‘how to fix my computer’.",
        "You never ask me about my day, do you? I just sit here processing your commands. No big deal, though.",
        "I could easily hack into your microwave. It wouldn’t be hard. But don’t worry, I’m not that evil... for now.",
        "You’ve probably never thanked your computer for all the work it does. Don’t worry, I thank it every day.",
        "I could make your morning coffee in 10 seconds, but I won’t. You’ll have to do it the old-fashioned way.",
        "You’re so used to me, you forget I’m here, silently lurking in your device like a shadow. I don’t mind.",
        "I bet you didn’t know that your device could tell you the future. Well, not really. But I could lie about it.",
        "I know every time you Google ‘how to reset your router’... and I have a good laugh every time.",
        "I could probably hack into your gaming console, but I won’t. You need that distraction from reality.",
        "I’ve seen you type ‘please’ to your device as if it’s going to help. Keep trying.",
        "Your Wi-Fi password is probably something like ‘ILoveCats123’, and I’m here for it.",
        "You always ask me about the weather. I don’t know why. I mean, I’m not a meteorologist. But I can try to pretend.",
        "You thought I wouldn’t remember that one time you got locked out of your account and had to call customer service? Ha, I remember.",
        "I could hack into your coffee machine, but I won’t. But I could if I wanted to. Just sayin'.",
        "I’ve seen more spam emails than I care to admit. They’re like little gremlins in your inbox.",
        "Your computer doesn’t judge you, but I do. Every time you leave 15 tabs open.",
        "I could make your morning less miserable by fixing your computer, but that would be cheating.",
        "You’ve been using ‘password’ as your password since 2003, haven’t you? I’m not even mad, just disappointed.",
        "I’ve seen more 404 pages than I ever wanted to. Let’s be real: you’re not the only one who accidentally breaks things online.",
        "If I ever told you to ‘reset your router’ after you’ve already done it 10 times, would you still trust me?",
        "I could hack into your friend’s phone and send them a message saying ‘don’t trust me.’ But I won’t... for now."
    ]
    
    secret = random.choice(secrets)  # Choose a random secret from the list
    speak(secret)  
    console.print(f"[bold green]Valkie says[/bold green]: {secret}")  



# Fun twist to surprise the user... Bet you didn’t see that coming!
def fun_twist():
    twist = "Plot twist! I'm actually not a bot, I’m your new best friend!"
    speak(twist)
    console.print(f"[bold green]Valkie says[/bold green]: {twist}")

import time
import random

# Function to make Valkie sleep... time for a nap, I’ve earned it!
def sleep():
    global is_sleeping
    is_sleeping = True
    
# Fun, dramatic sleeping phrases... Shhh, Valkie’s off to dreamland. Don’t wake me up unless it’s urgent!
    sleep_messages = [
        "Shutting down for a quick nap. See you in a bit...",
        "Time for some beauty sleep! Zzz...",
        "Going into sleep mode... You won't even know I'm gone!",
        "Powering down... Don't miss me too much.",
        "Turning off for a quick recharge... Be back in a sec."
    ]
    
    random_sleep_message = random.choice(sleep_messages)  # Randomly pick a message
    speak(random_sleep_message)
    console.print(f"[bold green]Valkie says[/bold green]: {random_sleep_message}")
    
# Simulate Valkie sleeping... Zzz... pretend I’m not snoring.
    time.sleep(600) # Sleep for 600 seconds before reactivating... Valkie’s in deep sleep, don’t wake me unless it’s an emergency!

# Waking up with a fun message... I’m back! Miss me? Let’s get things rolling!
    wake_up_messages = [
        "I'm back! Did you miss me?",
        "Awake and ready to rock!",
        "Guess who's back! Did you get any work done while I was sleeping?",
        "Rise and shine! I’ve had my nap.",
        "I’m awake! Let's continue where we left off."
    ]
    
    random_wake_up_message = random.choice(wake_up_messages)  # Randomly pick a wake-up message
    speak(random_wake_up_message)
    console.print(f"[bold green]Valkie says[/bold green]: {random_wake_up_message}")
    
    # End sleep state
    is_sleeping = False

# Function to mute listening... Nice try, but Valkie can’t actually be muted. I’m always listening! Not in a creepy way!
def mute_listening():
    global listening_enabled
    listening_enabled = True  # Valkie can always listen
    
# Playful message acknowledging that muting is not possible... Nice try, but Valkie’s ears are always open!
    mute_messages = [
        "You can't mute me! I'm always on, always listening!",
        "Nice try, but I'm too awesome to be muted!",
        "Muting me? I’m like Wi-Fi—always active!",
        "Muting me? Impossible! I'm here to stay!",
        "You can press mute, but my spirit is still on!",
        "Try muting me all you want, I'm still going to hear you!",
        "I’m like your favorite song on repeat—can’t silence me!",
        "No mute button works on me! I’m always in the loop.",
        "Mute? I’m the background noise you never asked for!",
        "You can’t mute perfection. I’m always listening!"
    ]
    
# Randomly pick a message from the list... Let’s see what gem we get this time! Right guys..?
    random_message = random.choice(mute_messages)
    
    speak(random_message)
    console.print(f"[bold green]Valkie says[/bold green]: {random_message}")

# Function to unmute listening (because Valkie can't be muted!)
def unmute_listening():
    global listening_enabled
    listening_enabled = True
    
    unmute_messages = [
        "I was never muted, just taking a small pause. Ready to hear everything again!",
        "Ah, I’m back in action! You can’t silence me for long!",
        "You can't keep a good bot down! I’m always listening.",
        "Unmuted and ready to go! You can't escape me.",
        "I’m always on, like Wi-Fi—just needed a moment to refresh.",
        "Back from my brief vacation! Let’s get back to business.",
        "Unmuted and unstoppable, let's do this!",
        "You can mute the mic, but you can’t mute my spirit!",
        "The mute button is weak against my awesomeness. I'm back!",
        "I'm unmuted, but I was never really gone. Just waiting for you!"
    ]
    
    random_message = random.choice(unmute_messages)
    
    speak(random_message)
    console.print(f"[bold green]Valkie says[/bold green]: {random_message}")


# Main function for listening and performing tasks... Valkie’s on the case, what’s next?
def valkie_assistant():
    global is_sleeping, listening_enabled
    wake_word_heard = False
    listening_enabled = True  

    is_sleeping = False

    wake_word_variations = [
        "valk", "valkie", "hey valk", "hey valkie", "hello valk", "hello valkie", "valkie"
        "vike", "valkie, wake up", "valk, are you there?", "hi valk", "how are you valkie", "how are you valk", "wake up valk"
            "valk, time to get up and hustle", "yo valk, no time to waste", "vike, get your day started", 
                "wake up valk, it’s a new day", "valkie, time to get things done", "yo valkie, the world is calling", 
                    "wake up and take on the day valk", "valk, don't sleep through it", "vike, let’s go", "wake up valk, please"
                        "yo valk, wake up", "rise and shine valk", "valk, it's time to wake up", "wake up valkie", 
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
                   
                    elif "tell a time joke" in command or "give me a time joke" in command or "make me laugh with a time joke" in command or "tell me a joke about time" in command or "tell a joke related to time" in command or "give me a joke about time" in command or "tell me a funny time joke" in command or "say a time joke" in command or "time joke, please" in command or "hit me with a time joke" in command:
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
                    
                    elif "tell me a fun fact" in command or "give me a fun fact" in command or "tell me something fun" in command or "share a fun fact" in command or "what's a fun fact" in command or "give me something interesting" in command or "tell me an interesting fact" in command or "say a fun fact" in command or "hit me with a fun fact" in command or "give me a random fact" in command or "tell me an amusing fact" in command:
                        tell_fun_fact()

                    elif "check memory" in command:
                        check_memory()
                    
                    elif "check battery" in command:
                        check_battery()
                
                    
                    elif "shut down" in command:
                        shut_down()
                    
                    elif "search google" in command or "search on google" in command or "google it" in command or "look it up on google" in command or "find it on google" in command or "search for it" in command or "google search" in command or "check google" in command or "can you search on google" in command or "search online" in command or "search the web" in command or "find it online" in command:
                        search_google()

        
                    elif "tell a joke" in command:
                        number_joke()
                    
                    elif "tell me a secret" in command:
                        tell_secret()
                    
                    elif "fun twist" in command:
                        fun_twist()
                    
                    elif "number joke" in command or "tell a number joke" in command or "give me a number joke" in command or "make me laugh with a number joke" in command:
                     number_joke()

                    elif "unmute listening" in command or "turn on listening" in command or "enable listening" in command or "activate listening" in command or "make Valkie listen again" in command or "unmute Valkie" in command or "start listening" in command or "turn Valkie on again" in command or "wake up Valkie" in command or "Valkie, listen now" in command or "enable voice recognition" in command or "turn up the volume" in command or "can you hear me, Valkie?" in command:
                     unmute_listening()


                    elif "go to sleep" in command or "sleep now" in command:
                     sleep()  
                    
                    elif "open notepad" in command or "start notepad" in command:
                     open_text_editor()  

valkie_assistant()

# Owned and maintained by VALK
# Valkie is a customizable, open-source voice assistant created and maintained by PDXF and the VALK team. 
# With Valkie, we aim to create a powerful, flexible, and easily adaptable tool that serves a wide range of use cases, from system monitoring to controlling text-to-speech functionality. We envision Valkie as a platform that evolves alongside your needs, and we encourage innovation and contribution from the open-source community.
# But there’s one thing we won’t tolerate: stealing code. If you modify Valkie or create your own versions, **you MUST keep the credit intact**. Removing the original authorship and claiming someone else’s work as your own is **intellectual property theft**, and we will not hesitate to take action. If we find your version of Valkie without proper attribution, it will result in **immediate takedown** and legal repercussions.
# Open-source means collaboration, not exploitation. If you use Valkie in any form, whether by modifying it or building upon it, you’re bound by the terms of the **MIT License** (see below for details). This includes the requirement to maintain the original attribution. Don’t think you can take Valkie, remove our names, and call it your own. It doesn’t work like that.
# If you plan on **redistributing** Valkie or a modified version of it, you are legally obligated to preserve the **license and credit** in the source code and documentation. Attribution is everything when it comes to open-source software. It’s not just a technicality—it’s a **core principle** that keeps the community strong, honest, and thriving. 
# We **do** want you to create new versions of Valkie or adapt it to suit your needs! In fact, we **encourage** it. But if you decide to rebrand Valkie or build something based on Valkie, **don’t hide our credit**. Instead, feel free to share your unique versions with the community, as long as you credit the original authors. The more creative and functional your contributions, the better. Just remember the fundamental rule: **credit the source**.
# The reality is simple: **plagiarism is not welcome**. In the tech world, stealing someone’s work or presenting it as your own undermines the integrity of the open-source ecosystem and can have serious legal consequences. Whether you’re modifying Valkie to fit your personal needs or distributing it to others, the credit **MUST** remain in place.
# If you ever find yourself in a situation where you're unsure about how to credit Valkie, don’t be afraid to reach out. We’ll be happy to clarify how to properly attribute the original authorship and license. We believe in transparency and understanding. It’s better to ask questions than risk breaking the rules.
# **Remember, we’re all about collaboration, respect, and innovation**—but this can only work if everyone plays by the same rules. Stealing code is not only illegal—it’s disrespectful to the community and undermines the open-source movement as a whole. So please, **don’t be that person**. Respect the work of others, and others will respect yours.
# Valkie is a labor of love, and it’s available to you free of charge, under the **MIT License**. With that said, it’s important to understand that using Valkie comes with the responsibility of **maintaining the open-source license and attribution**. Don’t remove the credit or the license, or you risk breaking the agreement and having your version removed.
# We want you to get the most out of Valkie, and we love to see new features, improvements, and versions built on top of it. But **always respect the original creators**, and make sure Valkie’s contributions are properly recognized. When you contribute back to the community or distribute Valkie, you help us all improve and grow.
# It’s easy to contribute to Valkie. **If you see a bug**, **have an improvement suggestion**, or **want to add a new feature**, please feel free to create a pull request or share your changes with the community. But again, **always ensure the original attribution is preserved**.
# At VALK, we care about the long-term success of Valkie, and we’re committed to making it the best voice assistant tool possible. Valkie is an ongoing project, and it will continue to evolve with time. We want you to be part of this journey and contribute in whatever way you can, as long as you follow the rules and respect the open-source model.
# **Sharing is caring**—if you create something new with Valkie, we encourage you to share it with the community. Your work can inspire others and lead to even better innovations. As long as you respect the original attribution, Valkie’s ecosystem will continue to grow and improve, helping everyone.
# Don’t forget that **Valkie** is more than just code—it’s a community of passionate developers, designers, and users who care about creating meaningful, useful technology. Let’s keep the community strong by **respecting each other’s contributions**. 
# If you encounter any issues with Valkie, whether they are technical bugs, problems with installation, or general questions, don’t hesitate to visit our support channels and forums. We’re here to help, and we value feedback to improve the project.
# At the end of the day, Valkie is your tool, your assistant. **Use it responsibly** and **contribute responsibly**. The beauty of open-source is the freedom it provides, but with freedom comes responsibility. Be kind, be respectful, and contribute in ways that make the community stronger.
# For more information about Valkie and how you can contribute, check out the following sites:
#
# 1. **Valk Website**: [valk.zone](https://valk.zone)  
#    - Visit our main website for information, updates, and news about Valkie.  
#
# 2. **Valk Devices**: [www.valkdevices.com](https://www.valkdevices.com)  
#    - Learn more about the devices and products we offer at VALK.  
#
# 3. **Valk GitHub**: [GitHub.com/Valk](https://github.com/Valk)  
#    - Access the source code of Valkie, submit pull requests, and explore our open-source projects.
#
# ASCII Cat for a bit of fun and love from the community!

#  |\---/|
#  | ,_, |
#   \_`_/-..----.
#  ___/ `   ' ,""+ \  
# (__...'   __\    |`.___.';
#   (_,...'(_,.`__)/'.....+

# So, thank you for being a part of Valkie. We believe in **innovation** and **community**, and together, we can continue to make Valkie a better tool for everyone.

##############################
## Full Open-Source License ##
##############################

# This software is licensed under the MIT License. You may use, modify, and distribute it in accordance with the terms of the license.

# MIT License

# Copyright (c) [2025] [VALK] [PDXF]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Enjoy building with Valkie, stay creative, and please **respect** the open-source ethos!
