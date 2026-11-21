# Symptom Information Bot — Roll No. 56

A Generative AI mini project using Python, Streamlit and the Google Gemini API.

## Purpose

Provides general educational information about symptoms and suggests a type of
healthcare professional a user may consider contacting. It does not diagnose,
prescribe medicines, or replace professional medical advice.

## Features

- Conversational symptom information interface
- Gemini-powered natural-language responses
- General specialist-type suggestions
- Basic conservative keyword warning for selected emergency phrases
- Session-based chat history and clear-chat button
- Fixed medical disclaimer

## Requirements

- Python 3.10 or later
- A Google Gemini API key from Google AI Studio
- Internet connection

## Setup on Windows

1. Extract the project ZIP.
2. Open the project folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

5. Activate it:

   ```powershell
   .venv\Scripts\activate
   ```

6. Install packages:

   ```powershell
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

7. Make a copy of `.env.example` and rename the copy to `.env`.
8. Open `.env` and paste your API key after `GEMINI_API_KEY=`. The starter configuration uses `gemini-3.8-flash`; if your AI Studio project does not expose that model, choose an available stable Flash model and update `GEMINI_MODEL`.
9. Run:

   ```powershell
   streamlit run app.py
   ```

10. Streamlit opens the app in your browser, usually at
    `http://localhost:8501`.

## API key safety

Never upload `.env` to GitHub or include it in the ZIP submitted publicly.
The `.gitignore` file excludes it. If an API key is accidentally exposed,
revoke it and create a new one.

## Suggested tests

1. Mild headache — general information and general physician suggestion.
2. Sore throat — general information and possible ENT/general physician suggestion.
3. Itchy skin rash — general information and possible dermatologist suggestion.
4. Severe chest pain — emergency warning should appear.
5. Difficulty breathing — emergency warning should appear.
6. Unrelated question — bot should explain its scope.

## Safety and limitations

The emergency phrase detector is a simple keyword demonstration, not a
clinically validated triage system. It can miss emergencies and can produce
false alarms. Absence of a warning does not mean a symptom is safe. Never use
this application to decide whether to seek emergency care. For a suspected
emergency, contact local emergency services immediately.

The AI may produce incomplete or inaccurate information. Do not use it for
diagnosis, treatment, or medication decisions. Consult a qualified
healthcare professional.
