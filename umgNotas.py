# -*- encoding: utf-8 -*-
import requests
from pyquery import PyQuery



def umgNotas(user, pwd, sem, anio):

  payload = {
      'uid': user,
      'passwd': pwd
  }
  cusosList = []
  with requests.Session() as s:
    print "Ingresando, espera..."
    p = s.post('https://apps.umg.edu.gt/signup/', data=payload)
    # p = s.post('https://github.com/login', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    # print p.text

    datanota = {
      'c': sem,
      'y': anio
    }

    print "Obteniendo Notas, espera...."
    n = s.post('https://apps.umg.edu.gt/notas?v-n', data=datanota)

    q = PyQuery(n.text)

    
    cn = []

    for el in q('#marks tbody').items('tr'):
      
      for el2 in q(el).items('td'):
          cn += [el2.text()]
      cusosList += [cn]
      cn = []

    parseCursos = ""
    for cur in cusosList:
      parseCursos += "Curso: %s \nP#1: %s pts. \nP#2: %s pts. \nAct.: %s pts. \nFinal: %s pts. \nNota: %s pts. \n\n" %(cur[0], cur[1], cur[2], cur[3], cur[4], cur[5])



  return parseCursos
