from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# החלף בטוקן שקיבלת מ-BotFather
TOKEN = "YOUR_BOT_TOKEN_HERE" 

# --- פונקציות הבוט ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """שולח את השאלה הראשונה עם כפתורים."""
    
    # 1. הגדרת הכפתורים
    keyboard = [
        [
            InlineKeyboardButton("אפשרות א'", callback_data='option_a'),
            InlineKeyboardButton("אפשרות ב'", callback_data='option_b'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # 2. שליחת ההודעה עם הכפתורים
    await update.message.reply_text('שלום! אנא בחר אחת מהאפשרויות:', reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """מטפל בלחיצות על כפתורים."""
    
    query = update.callback_query
    
    # חובה לסיים את ה-callback
    await query.answer()

    # 3. בדיקה ופעולה לפי הבחירה
    if query.data == 'option_a':
        response_text = "בחרת באפשרות א'. הנה מידע נוסף..."
    elif query.data == 'option_b':
        response_text = "בחרת באפשרות ב'. עכשיו אשאל שאלה נוספת..."
        # ניתן להפעיל כאן פונקציה חדשה עם סט כפתורים חדש
    else:
        response_text = "אירעה שגיאה בבחירה."
        
    # 4. עריכת ההודעה המקורית או שליחת הודעה חדשה
    await query.edit_message_text(text=response_text)


# --- הרצת הבוט ---

def main() -> None:
    """הפונקציה הראשית שמריצה את הבוט."""
    
    # יצירת ה-Application
    application = Application.builder().token(TOKEN).build()

    # הוספת מטפלים לפקודות ולחיצות כפתורים
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    # הרצת הבוט (יפעל עד שתעצור אותו)
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()
