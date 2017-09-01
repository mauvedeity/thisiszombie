#!/usr/bin/python

import random
import os

def lenadjust(ch):
  return(ch * (random.randrange(20)+1)) # make sure we have at least one

def brains():
  return('bra' + (lenadjust('a')) + 'ins')

def cerveaux():
  return('cervea' + (lenadjust('a')) + 'ux')

def gehirne():
  return('Gehi' + (lenadjust('i')) + 'rne')

def cerebros():
  return('cerebr' + (lenadjust('o')) + 's')

def utterance():
  lang = random.randrange(10)
  if (lang > 3): lang = 0
  rv = {
    0: 'Bra' + (lenadjust('a')) + 'ins',
    1: 'Cervea' + (lenadjust('a')) + 'ux',
    2: 'Gehi' + (lenadjust('i')) + 'rne',
    3: 'Cerebr' + (lenadjust('o')) + 's'
  }[lang]
  rv = rv + ' #zombie'
  return(rv)

def post():
  this_utter = utterance()
  oscmd = '/usr/local/bin/ttytter.pl -keyf=thisiszombie -silent -status="' + this_utter + '"'
  os.system(oscmd)
  oscmd = '/usr/local/bin/dcled -b 0 -p 9 -m "' + this_utter + '"'
  os.system(oscmd)

post()
