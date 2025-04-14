import pandas as pd
import pywhatkit
import time
from datetime import datetime

# Carrega a planilha
df = pd.read_excel('data/TesteClientes.xlsx')

# Caminho do arquivo de log
log_path = 'envio_log.txt'

# Mensagem base com placeholder {nome}
mensagem_base = (
    "💖 Oi, {nome}! Tudo bem?\n\n"
    "A gente está com saudades de ver você por aqui! 🥹\n"
    "O Dia das Mães está chegando, e essa é a hora perfeita pra encontrar um presente marcante – "
    "com aquele brilho especial que só a Guzzatti tem! ✨\n\n"
    "Corre lá no nosso site e aproveita as novidades (tem coisa linda e com condições especiais 😍)\n\n"
    "🛍️ www.guzzatti.com.br\n"
    "🎁 Não deixa pra última hora!\n\n"
    "Com carinho,\n"
    "Equipe Guzzatti 🤍"
)

# Loop para envio
for index, row in df.iterrows():
    nome = row['Client Name']
    numero = str(row['Phone'])
    mensagem = mensagem_base.format(nome=nome)
    hora = datetime.now().strftime('%H:%M:%S')

    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=f"+{numero}",
            message=mensagem,
            wait_time=15,
            tab_close=True
        )
        log_msg = f"✅ Mensagem enviada para {nome} ({numero}) às {hora}"
        print(log_msg)
    except Exception as e:
        log_msg = f"❌ Erro ao enviar para {nome} ({numero}): {e}"
        print(log_msg)

    # Escreve no arquivo de log
    with open(log_path, 'a', encoding='utf-8') as log_file:
        log_file.write(log_msg + '\n')

    # Espera 2 minutos e 30 segundos
    time.sleep(150)
