from telegram import  Update
from telegram.ext import CallbackContext
from Buttons import *
from database import *




def start(update:Update, context:CallbackContext):
    update.message.reply_text("Assalomu alaykum Botimizga xush kelibsiz\n"
                              "Ro'yxatdan o'tish uchun FIO ni yuboring", reply_markup=ReplyKeyboardRemove())
    return 'state_name'

def command_name(update:Update, context:CallbackContext):
    text = update.message.text
    update.message.reply_text("Sizning ismi familyangiz "+text+"\n"
                                                               "Yaxshi endi telefon raqamingizni yuboring", reply_markup=phone_button())
    context.user_data['name'] = text
    return 'state_phone'

def command_phone(update:Update, context:CallbackContext):
    contact = update.message.contact
    phone_number = contact.phone_number
    context.user_data['phone'] = phone_number
    update.message.reply_text(f"Sizning Ismingiz: {context.user_data['name']}\n"
                              f"Sizning telefon raqamingiz: {phone_number}\n"
                              f"Endi esa viloyatingizni kiriting?")
    return 'state_viloyat'

def command_viloyat(update:Update, context:CallbackContext):
    text = update.message.text
    update.message.reply_html(f"Sizning ism familyangiz : <b>{context.user_data['name']}</b>\n"
                              f"Sizning raqamingiz: <b>{context.user_data['phone']}</b>\n"
                              f"Siznig viloyatingiz: <b>{text}</b>\n"
                              f"<b><i>Siz mufaqiyatli ro'yxatdan o'tingiz</i></b>")
    add_user(update.effective_user.id,context.user_data['name'],update.effective_user.first_name,context.user_data['phone'],text)

