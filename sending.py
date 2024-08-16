import production
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
""" """
flag = '0'
while flag == '0':
    production.main()
    flag = input('Prévia gerada. Podemos seguir com esse modelo? \n 0 - Não \n 1 - Sim ')
    
emails = [" "]


with open('HTML/exemplo.html', 'r',encoding='utf-8') as file:
    newsletter_html = file.read()
key = "API_KEY"

def mensagem(mail):
    message = Mail(
        from_email='filipe.rojo@solar21.com.br',
        to_emails=mail,
        subject='Sua Newsletter Solar acaba de chegar 💛☀️',
        html_content = newsletter_html)
    return message

for i in emails:
    sg = SendGridAPIClient(key)
    text = mensagem(i)
    response = sg.send(text)
    print('E-mail enviado para {}'.format(i))
