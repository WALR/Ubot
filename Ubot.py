# -*- encoding: utf-8 -*-

import telebot

TOKEN = '200471947:AAEvrDdbqrtzuEgg94z0EJtIj1UhTK4CDaw'
Ubot = telebot.TeleBot(TOKEN)

print "[System] Bot a iniciado."

#
#   Comandos
#

commands = ['/ayuda', '/fecha', '/notas']

@Ubot.message_handler(commands=['ayuda'])
def command_ayuda(message):
  Ubot.reply_to(message, "Hola %s, en que puedo ayudarte? \nesto comandos puedes utilizar: \n/ayuda\n/fecha\n/notas" % message.from_user.username )

# fecha
from fecha import fecha
@Ubot.message_handler(commands=['fecha'])
def command_fecha(m):
  fecha(m, Ubot)

# Notas UMG
from umgNotas import umgNotas
@Ubot.message_handler(commands=['notas'])
def command_notas(m):
  cid = m.chat.id
  text = m.text.split()

  if len(text)==5:
    print text[0]
    print len(text)
    notas = umgNotas(text[1], text[2], text[3], text[4])
    Ubot.send_message(cid, notas)
  else:
    resp = "Lo siento, necesito que tu usuario, password, periodo y año separado por espacion Ejemplo:\n /notas mrivasp mrivas123 1 2016"
    Ubot.send_message(cid, resp)


def listener(mensajes):
  for m in mensajes:
    # print m
    chat_id = m.chat.id
    if m.content_type == 'text':
      text = m.text
      # Ubot.send_message(chat_id,"Me copio de tu texto")
      # Ubot.send_message(chat_id, text)
      # Ubot.send_location(chat_id, 15.783471, -90.230759)

Ubot.set_update_listener(listener) #registrar la funcion listener  
Ubot.polling()

while True: #No terminamos nuestro programa  
  pass