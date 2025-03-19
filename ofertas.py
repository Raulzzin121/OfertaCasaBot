# Atualização para Python 3.12 - 18/03/2025
# Este é o código completo do bot @OfertaCasaBot

from telegram.ext import Application, CommandHandler
import schedule
import time
from datetime import datetime
import pytz
import os
import threading

# Token do bot (embutido diretamente - substitua apenas se mudar o token no BotFather)
TOKEN = "7221577597:AAGCUog99zG5h-hke20Z0RCdU4Sti7aWDJk"  # Substitua pelo token correto do BotFather

# Chat ID onde as mensagens serão enviadas (grupo @OfertaCasaBot)
CHAT_ID = "@OfertaCasaBot"

# Função para enviar a mensagem de oferta
def enviar_oferta(bot, job):
    try:
        bot.send_message(chat_id=CHAT_ID, text="Oferta do dia! confira nossas promoções às 08:00!")
        print(f"Mensagem enviada com sucesso em {datetime.now(pytz.UTC)}")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Função para o comando /start (agora assíncrona)
async def start(update, context):
    try:
        await update.message.reply_text("Olá! Eu sou o @OfertaCasaBot. Use-me para enviar ofertas ao grupo às 08:00. Aguardando...")
        print(f"Comando /start recebido de: {update.message.chat_id}")
    except Exception as e:
        print(f"Erro no comando /start: {e}")

# Função para verificar o agendamento em segundo plano
def verificar_agendamento():
    schedule.every().day.at("08:00").do(enviar_oferta, bot=application.bot, job=None)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Inicialização do bot
application = Application.builder().token(TOKEN).build()

# Adiciona o comando /start
application.add_handler(CommandHandler("start", start))

# Inicia o bot para receber comandos
print("Bot iniciado. Aguardando comandos e agendamento...")

# Inicia a verificação de agendamentos em uma thread separada
thread = threading.Thread(target=verificar_agendamento)
thread.start()

# Mantém o bot rodando indefinidamente
application.run_polling()