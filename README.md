rtl-sdr
turns your Realtek RTL2832 based DVB dongle into a SDR receiver
======================================================================

rtl_udp is a copy of rtl_fm with a special feature: It opens a udp control port (currently fixed to 6020) which takes commands like changing the frequency or mode. No need to restart :)

**[Credits to olgierd](http://qi.reddit.com/user/olgierd)**

##Usage:

python script **udpclient.py** for easy operation included.

**possible commands:**

* freq (./udpclient.py freq 101900000)
* mode (./udpclient.py mode 0 (for fm))
  * 0 = FM
  * 1 = AM
  * 2 = USB
  * 3 = LSB
* squelch (./udpclient.py squelch 0)
  * 0 = OFF
  * n = Value
* gain (./udpclient.py agc auto)
  * auto = Automatic
  * n = Gainvalue; 195 = 19.5db
* agc (./udpclient.py agc 1)
  * 0 = OFF
  * 1 = ON 


##Todo:

* configureable address & port
* UDP streaming for PCM data

##Original RTL-SDR Source:

For more information see:
http://sdr.osmocom.org/trac/wiki/rtl-sdr


