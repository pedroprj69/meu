from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7334537866:AAGnrIj2vCoC76EWIFotsBpxiApKyoLe4D8"


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "💳 Para acessar nosso grupo VIP, faça o pagamento via Pix:\n\n"
        "🔗 [PAGUE AQUI](https://widget.livepix.gg/embed/b93bc02d-b68c-4c2b-9383-38da866c801f)\n\n"
        "Após o pagamento, você será adicionado automaticamente ao grupo! 🚀"
    )

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
