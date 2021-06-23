from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("اليك 3 متطلبات لتنصيب بوت تليثون العرب (باللغة العربية):\n\n١- معرف التطبيق (APP_ID)\n٢- ايبي الدخول للتطبييق (API_HASH)\n\nتستطيع الحصول عليهما من خلال my.telegram.org\nاو من خلال البوت @scrapmanbot\n٣- رقم الهاتف (ادخله مع مفتاح الدولة مثلًا العراق +964)\n")
print("Telethon For Arabs 🤖 : http://T.ME/OORRR")

APP_ID = int(input(": من فضلك قم بأدخال معرف التطبيق (APP_ID)\n"))
API_HASH = input(": من فضلك قم بأدخال ايبي الدخول للتطبييق (API_HASH)\n")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.send_message("me", client.session.save())


#Edit and convert it to Arabic file by :
