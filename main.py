import smtplib
from email.message import EmailMessage

SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
SMTP_USER = "COLOQUE_SEU_USUARIO_SMTP_AQUI"  #Preciso trocar essa parte por valores reais
SMTP_PASSWORD = "COLOQUE_SUA_SENHA_SMTP_AQUI"   #Entre no Mailtrap → Email Sandbox → SMTP Settings / Show Credentials e procure as credenciais específicas do SMTP Sandbox.

DESTINATARIO = "lucas.00000854565@unicap.br"


def enviar_smtp():
    mensagem = EmailMessage()

    mensagem["From"] = '"Albert Einstein" <einstein@exemplo.test>'
    mensagem["To"] = DESTINATARIO
    mensagem["Subject"] = "Demonstração de SMTP"

    mensagem.set_content(
        """Olá, turma!

Esta mensagem foi enviada utilizando SMTP.

Ela foi criada em Python e transmitida para um servidor
SMTP real do Mailtrap.

O campo From desta mensagem foi definido como:

Albert Einstein <einstein@exemplo.test>

Isso demonstra que o campo From é um cabeçalho da mensagem
e, isoladamente, não comprova a identidade real do remetente.

Mecanismos como SPF, DKIM e DMARC são utilizados atualmente
para ajudar na autenticação e validação de mensagens.

Esta é uma demonstração acadêmica de Redes de Computadores.
"""
    )

    print("\n=== CONEXÃO SMTP ===")
    print(f"Servidor: {SMTP_HOST}")
    print(f"Porta: {SMTP_PORT}")

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as servidor:
        servidor.set_debuglevel(1)

        print("\n=== EHLO ===")
        servidor.ehlo()

        if servidor.has_extn("starttls"):
            print("\n=== STARTTLS ===")
            servidor.starttls()
            servidor.ehlo()

        print("\n=== AUTENTICAÇÃO ===")
        servidor.login(SMTP_USER, SMTP_PASSWORD)

        print("\n=== MAIL FROM ===")
        print("Envelope SMTP:", SMTP_USER)

        print("\n=== RCPT TO ===")
        print("Destinatário:", DESTINATARIO)

        print("\n=== DATA ===")
        print("Transmitindo mensagem...")

        servidor.send_message(
            mensagem,
            from_addr=SMTP_USER,
            to_addrs=[DESTINATARIO]
        )

        print("\nMensagem aceita pelo servidor SMTP.")


print("\n=== Demonstração SMTP ===")
print("1 - Executar envio SMTP")
print("0 - Sair")

opcao = input("\nEscolha: ").strip()

if opcao == "1":
    enviar_smtp()
elif opcao == "0":
    print("Encerrando.")
else:
    print("Opção inválida.")