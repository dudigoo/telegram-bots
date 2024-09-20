from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define a few command handlers. These usually take the two arguments update and context.
def start(update: Update, context: CallbackContext) -> None:
    # Define the menu options
    menu = [['Option 1', 'Option 2'], ['Option 3', 'Option 4']]
    reply_markup = ReplyKeyboardMarkup(menu, one_time_keyboard=True)

    # Send a message with the menu
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("7455273181:AAHXjFoF-uWpVPPrUA9W0L7SrEeOsMKoC8w")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
aaa
bbb
vvv
