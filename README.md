RFID Squeezebox
===============

I stuck a [MFRC522] based RFID reader board, a piezo speaker and a [NodeMCU]
ESP8266 device in a (3d printed) [box]. I initially made an Arduino-language
[rfid-squeezebox] implementation that allowed my kids to scan RFID cards on the
device and the [squeezebox] network audio player in their room would start
playing their bedtime stories.

This is a micropython port of the original project which has added some new
features such as allowing programming the current playlist into a scanned card
and pausing and resuming the playback.

[MFRC522]:         https://github.com/miguelbalboa/rfid
[NodeMCU]:         https://en.wikipedia.org/wiki/NodeMCU
[box]:             http://a360.co/2tmpJZs
[rfid-squeezebox]: https://github.com/jondye/rfid-squeezebox
[squeezebox]:      https://en.wikipedia.org/wiki/Squeezebox_(network_music_player)
