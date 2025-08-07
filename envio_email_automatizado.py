import stmplib
from email.mime.text import MIMEText

rem = 'luvizottodev@gmail.com'
senha = 'your_app_password' 
dest = 'stefani292005@gmail.com'

msg = MIMEText('Teste de envio de email automatizado')
msg['Subject'] = 'Email automatizado'
msg['From'] = rem
msg['To'] = dest   

with stmplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(rem, senha)
    server.sendmail(rem, dest, msg.as_string())
    print('Email enviado com sucesso!')