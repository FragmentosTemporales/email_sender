from smtp import EmailSender
from config import settings as s

email_receiver = s.email_receiver
email_sender = EmailSender("¡Hola desde Python! Este es un correo de prueba.", email_receiver)

if __name__ == "__main__":
    email_sender.send_email()