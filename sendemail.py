import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import pandas as pd


def send_email(data):
    addr_from = "sysoevdaniil@mail.ru"
    addr_to = "cryp.sys.d@mail.ru"
    password = "QauKPLfjw9irFk9u51Ny"

    file = "тест.xlsx"
    blank = {"Клиент": [data[0]], "Название угля": [data[1]], "Количество угля": [data[2]], "Способ оплаты": [data[3]], "Сумма оплаты": [data[4]], "Адрес": [data[5]], "Время": [data[6]], "Телефон": [data[7]], "Комментарий": [data[8]]}
    df = pd.DataFrame(blank)
    df.to_excel(file)

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    date = datetime.datetime.now()
    datenow = "{0}.{1}.{2}".format(date.day, date.month, date.year)
    msg['Subject'] = 'Заявка от ' + datenow
    att1 = MIMEText(open("тест.xlsx", 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    blank_name = datenow + ".xlsx"
    att1["Content-Disposition"] = 'attachment; filename=' + blank_name
    msg.attach(att1)

    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()