# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "flask",
# ]
# ///

# uv: requirements = ["flask"]

import random

from flask import Flask

app = Flask(__name__)

jokes_facts = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Python was named after Monty Python, not the snake.",
    "A group of flamingos is called a 'flamboyance'.",
    "Did you know? The first computer bug was an actual moth.",
    "UV makes Python fast and fun! 😎",
    "You are awesome! Have a great day! 🌟",
    "Why did the developer go broke? Because he used up all his cache.",
    "The plural of 'octopus' is 'octopuses', not 'octopi'.",
    "In Python, whitespace matters!",
    "The world's first website is still online: info.cern.ch",
]


@app.route("/")
def home():
    return {"message": random.choice(jokes_facts)}


if __name__ == "__main__":
    app.run(port=5000)
