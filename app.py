from config import PhotoQr, Scan
from setting import bot


@bot.message_handler(content_types=['photo'])
def do_qr(message):
    PhotoQr.photo_detect(message)


@bot.message_handler(content_types=['text'])
def do_text(message):
    Scan.scan(message)


bot.polling()
