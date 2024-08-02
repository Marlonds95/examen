import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from credenciales_correo import usuario_correo, contraseña_correo

def enviar_correo(destinatario, asunto, cuerpo):
    # Servidor SMTP
    servidor_smtp = "smtp.gmail.com"
    puerto_smtp = 587

    # Mensaje de correo
    mensaje = MIMEMultipart()
    mensaje['From'] = usuario_correo
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Conecta al servidor SMTP y envía el correo
    try:
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()
        servidor.login(usuario_correo, contraseña_correo)
        servidor.sendmail(usuario_correo, destinatario, mensaje.as_string())
        servidor.quit()
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

# Aplicación
destinatario = "123test12345@yopmail.com"
asunto = "Prueba de correo desde Python"
cuerpo = "Hola, esto es un mensaje de prueba desde Python."

enviar_correo(destinatario, asunto, cuerpo)