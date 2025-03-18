# Atualização para Python 3.12 - 18/03/2025
# Este é o código completo do bot @OfertaCasaBot

import telegram
from telegram.ext import Updater, CommandHandler, JobQueue
import schedule
import time
from datetime import datetime
import pytz
import os
import threading

# Token do bot (embutido diretamente - substitua apenas se mudar o token no BotFather)
TOKEN = "7221577597:AAFGhtg9PXge8XEQSVevYxEJuaHJXxIahH0"

# Chat ID onde as mensagens serão enviadas (grupo @OfertaCasaBot)
CHAT_ID = "@OfertaCasaBot"

# Função para enviar a mensagem de oferta
def enviar_oferta(bot, job):
    try:
        bot.send_message(chat_id=CHAT_ID, text='Oferta do dia! Confira nossas promoções às 08:00!')
        print(f"Mensagem enviada com sucesso em {datetime.now(pytz.utc)} UTC")
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

# Função para o comando /start
def start(update, context):
    try:
        update.message.reply_text('Olá! Eu sou o @OfertaCasaBot. Use-me para enviar ofertas ao grupo às 08:00. Aguardando...')
        print(f"Comando /start recebido de: {update.message.chat_id}")
    except Exception as e:
        print(f"Erro no comando /start: {e}")

# Função para verificar o agendamento em segundo plano
def verificar_agendamento():
    schedule.every().day.at("08:00").do(enviar_oferta, bot=updater.bot, job=None)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Inicialização do bot
updater = Updater(TOKEN)
dp = updater.dispatcher

# Adiciona o comando /start
dp.add_handler(CommandHandler("start", start))

# Inicia o bot para receber comandos
updater.start_polling()
print("Bot iniciado. Aguardando comandos e agendamento...")

# Inicia a verificação de agendamento em uma thread separada
thread = threading.Thread(target=verificar_agendamento)
thread.start()

# Mantém o bot rodando indefinidamente
updater.idle()