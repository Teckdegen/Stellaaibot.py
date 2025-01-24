from flask import Flask
import threading
import time
import os

app = Flask("KeepAliveApp")

@app.route("/")
def home():
    return "Bot is alive!"

def run_flask():
    """Run the Flask app to keep the bot alive"""
    app.run(host="0.0.0.0", port=8080)

def start_bot():
    """Start the bot (replace with your bot's entry point)"""
    os.system("python bot.py")  # Replace 'bot.py' with the actual file running your bot

if __name__ == "__main__":
    # Start the Flask app in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True  # Allows the thread to exit when the main program exits
    flask_thread.start()
    
    # Start the bot
    start_bot()

