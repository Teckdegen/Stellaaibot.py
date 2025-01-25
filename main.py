import telebot
from groq import Groq
from Keep_alive import keep_alive
keep_alive()
# Set your Groq API key directly
GROQ_API_KEY = "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"  # Replace with your actual API key
API_TOKEN = '7854835783:AAFODdPMu8Wd28uXf8KD2DYCKxKY_6ad53U'  # Replace with your actual Telegram bot token

# Initialize the Groq client
client = Groq(api_key=GROQ_API_KEY)

# Initialize the Telegram bot
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "I'm Teck AI assistant Chatbot. How can I assist you today?")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_message = message.text
    try:
        # Call Groq to generate a response
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_message},
            ],
            model="llama-3.3-70b-versatile",  # Specify the Groq model
        )

        # Extract the AI-generated reply
        ai_reply = chat_completion.choices[0].message.content

        # Send the reply back to the user
        bot.reply_to(message, ai_reply)

    except Exception as e:
        # Handle errors gracefully
        bot.reply_to(message, f"Sorry, I encountered an error: {str(e)}")

# Start polling for messages
bot.polling()
