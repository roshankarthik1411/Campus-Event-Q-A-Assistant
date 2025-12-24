import json

EVENTS = {
    "tech fest": {
        "event_name": "Tech Fest",
        "date": "2025-09-15",
        "location": "Main Auditorium",
    },
    "career fair": {
        "event_name": "Career Fair",
        "date": "2025-10-20",
        "location": "Student Center",
    },
    "hackathon": {
        "event_name": "Hackathon",
        "date": "2025-11-10",
        "location": "Computer Science Building",
    },
    "music concert": {
        "event_name": "Music Concert",
        "date": "2025-12-05",
        "location": "Campus Amphitheater",
    }
}

def ask_assistant(user_query: str):
    query = user_query.lower()

    for key, event in EVENTS.items():
        if key in query:
            return {
                "event_name": event["event_name"],
                "date": event["date"],
                "location": event["location"],
                "response": f"The {event['event_name']} will be held on {event['date']} at the {event['location']}."
            }

    return "I'm here to help with campus events! Ask me about Tech Fest, Career Fair, Hackathon, and more."
