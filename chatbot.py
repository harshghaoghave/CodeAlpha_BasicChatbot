import random
import time

# ─────────────────────────────────────────────
#  Response rules: keyword → list of replies
# ─────────────────────────────────────────────
RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "howdy", "hiya"): [
        "Hey there! 👋",
        "Hi! How can I help you?",
        "Hello! Great to see you!",
    ],
    # Farewells
    ("bye", "goodbye", "see you", "later", "exit", "quit"): [
        "Goodbye! Take care 👋",
        "See you later!",
        "Bye! Have a great day!",
    ],
    # How are you
    ("how are you", "how r you", "how are u", "you okay", "you good"): [
        "I'm doing great, thanks for asking! 😊",
        "All good on my end! How about you?",
        "Feeling fantastic! What's up?",
    ],
    # Name
    ("your name", "who are you", "what are you", "what's your name"): [
        "I'm PyBot, your friendly Python chatbot! 🤖",
        "They call me PyBot. Nice to meet you!",
    ],
    # Thanks
    ("thank you", "thanks", "thx", "ty"): [
        "You're welcome! 😊",
        "Happy to help!",
        "Anytime!",
    ],
    # Help
    ("help", "what can you do", "commands"): [
        "I can chat! Try saying: hello, how are you, your name, joke, time, or bye.",
    ],
    # Joke
    ("joke", "tell me a joke", "funny", "make me laugh"): [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the Python script break up with Java? Too many type issues. 😄",
        "How many programmers does it take to change a light bulb? None — it's a hardware problem! 💡",
    ],
    # Time / date
    ("time", "what time", "date", "what's the date", "today"): [
        "__TIME__",   # special token — filled in at runtime
    ],
    # Mood
    ("sad", "unhappy", "depressed", "not good", "not okay"): [
        "I'm sorry to hear that. 😢 Hope things get better soon!",
        "Hang in there! You've got this. 💪",
    ],
    ("happy", "great", "good", "awesome", "fantastic", "wonderful"): [
        "That's amazing to hear! 🎉",
        "Awesome! Keep that energy going! ⚡",
    ],
}

UNKNOWN_REPLIES = [
    "Hmm, I'm not sure I understand. Try 'help' to see what I can do.",
    "I didn't quite catch that. Type 'help' for options!",
    "I'm still learning! Could you rephrase that?",
]


# ─────────────────────────────────────────────
#  Core functions
# ─────────────────────────────────────────────

def get_response(user_input):
    """Match user input against keyword rules and return a reply."""
    text = user_input.lower().strip()

    for keywords, replies in RESPONSES.items():
        for keyword in keywords:
            if keyword in text:
                reply = random.choice(replies)
                # Handle special runtime token
                if reply == "__TIME__":
                    reply = f"It's {time.strftime('%I:%M %p')} on {time.strftime('%A, %d %B %Y')} 🕐"
                return reply

    return random.choice(UNKNOWN_REPLIES)


def is_farewell(user_input):
    """Check if the user wants to exit."""
    farewells = ("bye", "goodbye", "see you", "later", "exit", "quit")
    text = user_input.lower().strip()
    return any(word in text for word in farewells)


def typing_effect(text, delay=0.03):
    """Print text with a subtle typing effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def chat():
    """Main chat loop."""
    print("\n" + "=" * 44)
    print("         🤖 PyBot — Simple Chatbot")
    print("=" * 44)
    print("  Type 'help' for options, 'bye' to quit.\n")

    while True:
        try:
            user_input = input("  You   : ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  PyBot : Caught a keyboard interrupt — bye! 👋\n")
            break

        if not user_input:
            print("  PyBot : (Type something — I'm listening!)")
            continue

        response = get_response(user_input)
        print("  PyBot : ", end="")
        typing_effect(response)
        print()

        if is_farewell(user_input):
            break

    print("=" * 44 + "\n")


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    chat()
