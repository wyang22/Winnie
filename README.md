Winnie
=====================================

Winnie is a home robot project developed by me in my spare time. She is composed by 4 wheels, 2 robot arms and a neck to move cameras with the head freely.


<img src="https://github.com/wyang22/Winnie/blob/main/images/Winnie.jpg" alt="WinnieDemo" />



Step 1: Configure the robot to connect with WiFi automatically after power on
----------------

Connect robot chipset with internet cable, login to the system, and modify below file '/etc/network/interfaces' as below:

```
# interfaces(5) file used by ifup(8) and ifdown(8)

# Please note that this file is written to be used with dhcpcd
# For static IP, consult /etc/dhcpcd.conf and 'man dhcpcd.conf'

# Include files from /etc/network/interfaces.d:
source-directory /etc/network/interfaces.d

auto lo
iface lo inet loopback
iface eth0 inet manual
allow-hotplug wlan0
iface wlan0 inet static
wpa-ssid  LOCAL_NEWORK_SSID
wpa-psk  LOCAL_NEWORK_PASSWORD
address IPV4_ADRESS_FOR_ROBOT (eg. 10.0.0.7)
netmask 255.255.255.0
gateway DEFAULT_GATEWAY (eg. 10.0.0.1)
network 10.0.0.1
# wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

allow-hotplug wlan1
iface wlan1 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

Step 2: Connect your PC with robot
----------------
(1) Reboot the robot, wait until it connect to WiFi
(2) Connect to the robot using Putty with the right IP address
