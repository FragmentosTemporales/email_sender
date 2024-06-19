import smtplib
from email.message import EmailMessage
from config import settings as s

class EmailSender:
    def __init__(self, msg, receiver):
        self.message = EmailMessage()
        self.email_subject = "Prueba de correo desde Python"
        self.sender_email_address = s.email_user
        self.receiver_email_address = receiver
        self.password = s.email_password

        self.message['Subject'] = self.email_subject
        self.message['From'] = self.sender_email_address
        self.message['To'] = self.receiver_email_address

        self.message.set_content(msg)

        self.smtp_server = 'smtp.fastmail.com'
        self.smtp_port = 465

    def send_email(self):
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.sender_email_address, self.password)
                server.sendmail(self.sender_email_address, self.receiver_email_address, self.message.as_string())
                print("Correo enviado correctamente.")
        except smtplib.SMTPAuthenticationError:
            print("Error de autenticación. Verifica la contraseña y los detalles del servidor SMTP.")
        except smtplib.SMTPConnectError:
            print("Error de conexión. No se pudo conectar al servidor SMTP.")
        except smtplib.SMTPRecipientsRefused:
            print("El servidor SMTP rechazó al destinatario.")
        except smtplib.SMTPSenderRefused:
            print("El servidor SMTP rechazó la dirección del remitente.")
        except smtplib.SMTPDataError:
            print("Error de datos. El servidor SMTP respondió con un error inesperado.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
