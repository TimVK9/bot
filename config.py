import telebot
from telebot import TeleBot
import qrcode
from qreader import QReader
import cv2
from pathlib import Path
from setting import bot




class PhotoQr:

    @staticmethod
    def photo_detect(message):
        qreader = QReader()
        Path(f'files_scan/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = f'files_scan/{message.chat.id}/' + file_info.file_path.replace('photos/', '')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        image = cv2.cvtColor(cv2.imread(src), cv2.COLOR_BGR2RGB)
        decoded_text = qreader.detect_and_decode(image=image)
        for i in decoded_text:
            bot.send_message(message.chat.id, i)


class Scan:
    @staticmethod
    def scan(message):
        count = 0
        Path(f'files_user_text/').mkdir(parents=True, exist_ok=True)

        if message:
            count += 1
            qrcode.make(message.text).save(f'files_user_text/file_number{count}.png')

            with open(f'files_user_text/file_number{count}.png', 'rb') as i:
                bot.send_photo(message.chat.id, i)

