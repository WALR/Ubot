def fecha(m, bot):
  import datetime
  cid = m.chat.id
  x = datetime.datetime.now()
  switcher = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
  mes = switcher[x.month]
  anio = x.year
  fecha = "Hoy es %s de %s del %s" % (x.day, mes, anio)
  bot.send_message(cid, fecha)