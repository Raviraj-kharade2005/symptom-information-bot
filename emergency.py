"""
Conservative keyword-based safety flag.

This is only a basic educational safeguard, not a validated medical triage
system. It may miss emergencies and may flag phrases that are not emergencies.
The user interface always advises users not to rely on this app for triage.
"""

EMERGENCY_PHRASES = [
    "can't breathe",
    "cannot breathe",
    "difficulty breathing",
    "trouble breathing",
    "shortness of breath",
    "chest pain",
    "chest pressure",
    "severe bleeding",
    "uncontrolled bleeding",
    "unconscious",
    "passed out",
    "loss of consciousness",
    "not waking up",
    "face drooping",
    "one-sided weakness",
    "slurred speech",
    "sudden weakness",
    "seizure",
    "severe allergic reaction",
    "throat is closing",
    "blue lips",
]

def detect_emergency(text: str) -> dict:
    normalized = text.lower()
    matches = [phrase for phrase in EMERGENCY_PHRASES if phrase in normalized]
    if matches:
        return {
            "flagged": True,
            "matches": matches,
            "message": (
                "Your message contains wording that can be associated with "
                "a medical emergency. Contact local emergency services or "
                "go to the nearest emergency department now. Do not wait for "
                "an online chatbot response."
            ),
        }
    return {"flagged": False, "matches": [], "message": ""}
