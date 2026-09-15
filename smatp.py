from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# 1. Configurações do Servidor SMTP de Testes (ex: Mailtrap)
SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525  # ou 587
SMTP_USER = "seu_usuario_aqui"
SMTP_PASS = "sua_senha_aqui"

# 2. Definição da Mensagem
# O cabeçalho 'From' pode ser forjado com qualquer identidade fictícia ou famosa,
# mesmo que a conexão SMTP seja autenticada com sua conta de testes.
remetente_falso = "Albert Einstein <einstein@fisica.ox.ac.uk>"
destinatario = "turma@exemplo.com"
assunto = "Aviso importante sobre a Teoria da Relatividade"

corpo_html = """
<html>
  <body>
    <h2>Prezada Turma,</h2>
    <p>Escrevo para lembrar que o tempo é relativo, mas a entrega do trabalho prático de redes não é.</p>
    <p>Atenciosamente,</p>
    <p><b>Albert Einstein</b></p>
  </body>
</html>
"""

# 3. Construção do Objeto de E-mail
mensagem = MIMEMultipart("alternative")
mensagem["Subject"] = assunto
mensagem["From"] = remetente_falso
mensagem["To"] = destinatario

# Anexa o conteúdo HTML
mensagem.attach(MIMEText(corpo_html, "html"))

# 4. Conexão e Envio via smtplib
try:
  print("Conectando ao servidor SMTP...")
  with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as servidor:
    servidor.starttls()  # Ativa criptografia TLS se suportada
    servidor.login(SMTP_USER, SMTP_PASS)

    print("Enviando e-mail...")
    servidor.sendmail(
        remetente_falso, destinatario, mensagem.as_string()
    )

  print("E-mail enviado com sucesso! Verifique a caixa de entrada do Mailtrap.")

except Exception as e:
  print(f"Erro ao enviar o e-mail: {e}")