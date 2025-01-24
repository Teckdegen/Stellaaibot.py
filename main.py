from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

# Bot Metadata
"""
Bot Name: Stella - AI Therapist
Version: 1.1
Description: A friendly AI therapist bot to provide a listening ear and support to users.
"""

# Initialize the Groq API client
client = Groq(api_key="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")

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Sends a welcome message to the user when they initiate the bot.
    """
    welcome_message = (
        "Hello! 😊\n\n"
        "I'm Stella, your AI Therapist. I'm here to provide a listening ear and help you navigate your thoughts. "
        "Feel free to share anything with me. Let's start this journey together! 🌟"
    )
    await update.message.reply_text(welcome_message)

# Define a helper function to interact with the AI API
async def get_ai_response(user_input: str) -> str:
    """
    Interacts with the Groq AI API to generate a response based on user input.
    :param user_input: The user's message to the bot.
    :return: The AI-generated response.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "I'm sorry, I encountered an error while processing your message. Please try again later."

# Define a message handler for user input
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles user messages and provides an AI-generated response.
    """
    user_message = update.message.text
    ai_response = await get_ai_response(user_message)
    await update.message.reply_text(ai_response)

def main():
    """
    Main function to start the Telegram bot.
    """
    # Replace with your actual bot token
    token = "7820337311:AAF2cqmDKe-1LOtrCrKDAceWcRNOYlaLQKY"

    # Initialize the application
    application = Application.builder().token(token).build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Add the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    try:
        print("Stella is now running... 🚀")
        application.run_polling()
    except Exception as e:
        print(f"Error occurred while running the bot: {e}")

if __name__ == "__main__":
    main()
