#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket, sys

if len(sys.argv) < 3:
	sys.exit(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("localhost", 6020))

buf = ""

mode = sys.argv[1]
data = int(sys.argv[2])

if mode == 'freq':
	buf = buf + chr(0)
elif mode == 'mode':
	buf = buf + chr(1)
elif mode == 'squelch':
  buf = buf + chr(2)
else:
	sys.exit(1)

i=0
while i < 4:
	buf = buf + chr(data & 0xff)
	data = data >> 8
	i = i + 1


s.send(buf)
s.close()
