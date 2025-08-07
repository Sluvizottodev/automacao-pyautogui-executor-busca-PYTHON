import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv  # <-- aqui

load_dotenv()  # carrega as variáveis do .env

rem = 'luvizottodev@gmail.com'
senha = os.getenv('EMAIL_APP_PASSWORD')
print('Senha obtida:', senha)  
dest = 'stefani292005@gmail.com'

msg = MIMEText('Teste de envio de email automatizado')
msg['Subject'] = 'Email automatizado'
msg['From'] = rem
msg['To'] = dest   

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(rem, senha)
    server.sendmail(rem, dest, msg.as_string())
    print('Email enviado com sucesso!')
