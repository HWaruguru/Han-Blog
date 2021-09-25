from flask import render_template
from app import app

# Views
@app.route("/")
def index():
    blogs = [
        {
            "title": "When the biggest Disruption is to just sit down and focus",
            "content": "If I had to distill a singular takeaway from the hours of programming, demo floor and Startup Battlefield, it would be this: Disruption needs direction. We’re in the middle of unprecedented times, and while that’s been good news for some entrepreneurs (and bad news for very many), focus may be what leads us out of it.",
            "author": "Natasha Mascarenhas",
            "date": "September 25, 2021",
            "heart": 1
        },
        {
            "title": "When the biggest Disruption is to just sit down and focus",
            "content": "If I had to distill a singular takeaway from the hours of programming, demo floor and Startup Battlefield, it would be this: Disruption needs direction. We’re in the middle of unprecedented times, and while that’s been good news for some entrepreneurs (and bad news for very many), focus may be what leads us out of it.",
            "author": "Natasha Mascarenhas",
            "date": "September 25, 2021",
            "heart": 1
        },
        {
            "title": "When the biggest Disruption is to just sit down and focus",
            "content": "If I had to distill a singular takeaway from the hours of programming, demo floor and Startup Battlefield, it would be this: Disruption needs direction. We’re in the middle of unprecedented times, and while that’s been good news for some entrepreneurs (and bad news for very many), focus may be what leads us out of it.",
            "author": "Natasha Mascarenhas",
            "date": "September 25, 2021",
            "heart": 1
        },
        {
            "title": "When the biggest Disruption is to just sit down and focus",
            "content": "If I had to distill a singular takeaway from the hours of programming, demo floor and Startup Battlefield, it would be this: Disruption needs direction. We’re in the middle of unprecedented times, and while that’s been good news for some entrepreneurs (and bad news for very many), focus may be what leads us out of it.",
            "author": "Natasha Mascarenhas",
            "date": "September 25, 2021",
            "heart": 1
        },
        {
            "title": "When the biggest Disruption is to just sit down and focus",
            "content": "If I had to distill a singular takeaway from the hours of programming, demo floor and Startup Battlefield, it would be this: Disruption needs direction. We’re in the middle of unprecedented times, and while that’s been good news for some entrepreneurs (and bad news for very many), focus may be what leads us out of it.",
            "author": "Natasha Mascarenhas",
            "date": "September 25, 2021",
            "heart": 1
        }
    ]
    
    quote = {"quote": "Perl – The only language that looks the same before and after RSA encryption.", "author": "Keith Bostic"}

    return render_template("index.html", blogs=blogs, quote=quote)
