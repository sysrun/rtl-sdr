#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# * UDP modifications: Original Code by Olgierd Pilarczyk
# * Extended by Frederik Granna <rtlsdr@granna.de>
#
import socket, sys

if len(sys.argv) < 3:
	sys.exit(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 6020))

buf = ""

mode = sys.argv[1]
data = sys.argv[2]

if mode == 'freq':
	buf = buf + chr(0)
elif mode == 'mode':
	buf = buf + chr(1)
elif mode == 'squelch':
  buf = buf + chr(2)
elif mode == 'gain':
  buf = buf + chr(3)
  if data == 'auto':
    data = -100
elif mode == 'srate':
  buf = buf + chr(4)
elif mode == 'orate':
  buf = buf + chr(5)
elif mode == 'agc':
  buf = buf + chr(8)
  if data == 'on':
    data = 1
  elif data == 'off':
    data = 0

else:
	sys.exit(1)

data = int(data)

i=0
while i < 4:
	buf = buf + chr(data & 0xff)
	data = data >> 8
	i = i + 1


s.send(buf)
s.close()
