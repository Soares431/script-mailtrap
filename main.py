import smtplib
from email.message import EmailMessage
import date
import logging 
import time

SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
SMTP_USER = date.USER  
SMTP_PASSWORD = date.PASSWORD 

DESTINATARIO = "lucas.00000854565@unicap.br"


def enviar_smtp():
    mensagem = EmailMessage()

    mensagem["From"] = '"Neyma" <meninoney@exemplo.test>'
    mensagem["To"] = DESTINATARIO
    mensagem["Subject"] = "Demonstração de SMTP"

    mensagem.set_content(
        """Olá, turma!

Esta mensagem foi enviada utilizando SMTP.

Ela foi criada em Python e transmitida para um servidor
SMTP real do Mailtrap.

O campo From desta mensagem foi definido como:

Meu menino Ney <einstein@exemplo.test>

Isso demonstra que o campo From é um cabeçalho da mensagem
e, não comprova a identidade do remetente.

Mecanismos como SPF, DKIM e DMARC são utilizados atualmente
para ajudar na autenticação e validação de mensagens.

Esta é uma demonstração acadêmica de Redes de Computadores.
"""
    )

    print("\n=== SIMULAÇÃO DE ENVIO DE E-MAIL E CONEXÃO SMTP ===")
    print(f"Servidor: {SMTP_HOST}")
    print(f"Porta: {SMTP_PORT}")
    time.sleep(3)
    
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as servidor:
        servidor.set_debuglevel(1)

        logging.log(logging.INFO, "\n=== EHLO ===")
        servidor.ehlo()
        time.sleep(1)

        if servidor.has_extn("starttls"):
            logging.log(logging.DEBUG, "\n=== STARTTLS ===")
            servidor.starttls()
            servidor.ehlo()

        logging.log(logging.INFO, "\n=== AUTENTICAÇÃO ===")
        servidor.login(SMTP_USER, SMTP_PASSWORD)

        logging.log(logging.INFO, "\n=== MAIL FROM ===")
        logging.log(logging.INFO, "Envelope SMTP: {}".format(SMTP_USER))

        logging.log(logging.INFO, "\n=== RCPT TO ===")
        logging.log(logging.INFO, "Destinatário: {}".format(DESTINATARIO))

        logging.log(logging.INFO, "\n=== DATA ===")
        logging.log(logging.INFO, "Transmitindo mensagem...")
        time.sleep(5)

        servidor.send_message(
            mensagem,
            from_addr=SMTP_USER,
            to_addrs=[DESTINATARIO]
        )

        logging.log(logging.INFO, "\nMensagem aceita pelo servidor SMTP. - ENVIO CONCLUÍDO")
        


print("\n=== Demonstração SMTP ===")
print("1 - Executar envio SMTP")
print("0 - Sair")
print("=========================")


opcao = input("\nEscolha: ").strip()

if opcao == "1": enviar_smtp()
elif opcao == "0": logging.log(logging.WARNING, "Encerrando.")
else:  logging.error("Opção inválida.")