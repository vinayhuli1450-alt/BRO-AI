BRO AI — Starter Project

WHAT'S INCLUDED
- Premium dark blue/purple chat interface
- Python FastAPI backend
- Generic OpenAI-compatible chat-completions API connection
- Browser speech input (where supported)
- Browser text-to-speech with a female voice preference (voice availability depends on the device/browser)

RUN ON A LAPTOP
1. Install Python 3.10 or newer.
2. Extract this ZIP.
3. Open a terminal in the BRO_AI_starter folder.
4. Create a virtual environment:
   Windows: py -m venv .venv
   macOS/Linux: python3 -m venv .venv
5. Activate it:
   Windows PowerShell: .venv\Scripts\Activate.ps1
   Windows CMD: .venv\Scripts\activate.bat
   macOS/Linux: source .venv/bin/activate
6. Install packages:
   pip install -r requirements.txt
7. Copy .env.example to a new file named .env.
8. Fill in AI_API_KEY, AI_API_URL, and AI_MODEL using the details from your chosen provider.
9. Start the app:
   uvicorn app:app --reload
10. Open http://127.0.0.1:8000 in your browser.

IMPORTANT
- Without API settings, the interface runs but gives a setup message instead of AI-generated answers.
- API providers may charge for usage. Check the provider's pricing before using it.
- Never share your .env file or API key.
- To use it on your phone, both devices can be on the same Wi-Fi and you can open the laptop's local network address in the phone browser. For access from anywhere, deploy it securely to a hosting service and use HTTPS.
- Speech recognition support varies by browser. Chrome usually has better support than some mobile browsers.
- The female voice is selected from voices available on the user's device; the app cannot guarantee the exact same voice on every phone or computer.
