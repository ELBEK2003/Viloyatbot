from telegram import  Update
from telegram.ext import CallbackContext
from Buttons import *
from database import *




def start(update:Update, context:CallbackContext):
    if chek_user(update.effective_user.id):
        update.message.reply_text("Salom",reply_markup=main_buttons())
        return 'state_main'
    print(salom)
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
    try:
        contact = update.message.contact
        phone_number = contact.phone_number
    except Exception as e:
        phone=update.message.text
        if (phone[0]=='+' and len(phone)==13 and (phone[1:4]=='998') or phone[:3]=='998' and len(phone)==12) or (len(phone)==9):
            phone_number=phone
        else:
            update.message.reply_text('Siz telfon raqamingizni xato kiritizgiz qayat UZB nomer kiritib koring:')
            return 'state_phone'

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
    update.message.reply_html(" Buyurtmani birga joylashtiramiz",reply_markup=main_buttons())
    add_user(update.effective_user,context.user_data['name'],update.effective_user.first_name,context.user_data['phone'],text)
    return 'state_main'

def commandd_category(update:Update,context:CallbackContext):
    query=update.callback_query
    data=str(query.data)
    query.message.delete()

    if data.isdigit():
        cat_name=get_products_by_catid(int(data))[0]
        query.message.reply_photo(open('images/img.png','rb'),caption=f"Bo'lim <b>{cat_name}</b>",parse_mode="HTML",reply_markup=product_button_bycat(int(data)))







