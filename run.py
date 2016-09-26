import subprocess
import os
home = '/home/pi'
server = 'Public/NodeJS-Server'
print ('Installing git-core\n')
subprocess.call(['sudo','apt-get','install','-y','git-core'])

print ('\nCloning wiringPi\n')
subprocess.call(['git','clone','git://git.drogon.net/wiringPi'])

print ('\nInstalling Wiring-Pi\n')
os.chdir('/wiringPi')
subprocess.call('sudo ./build', shell=True)
os.chdir(home)

'''print ('\nInstalling 433Utils\n')
subprocess.call('mkdir /433Utils | git clone --recursive git://github.com/ninjablocks/433Utils.git ~/433Utils', shell=True)
subprocess.call('cd /433Utils/RPi_utils | make', shell=True)'''

print ('\nInstalling XRDP\n')
subprocess.call(['sudo','apt-get','install','-y','xrdp'])

print ('\nInstalling NodeJS')
subprocess.call('curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -', shell=True)
subprocess.call(['sudo','apt-get','install','-y','nodejs'])

print ('\nInstalling WirelessHome Server\n')
subprocess.call('mkdir /home/pi/Public/NodeJS-Server | git clone git://github.com/maodijim/NodeJS-Server Public/NodeJS-Server', shell=True)

print ('\nInstalling PM2\n')
subprocess.call('sudo npm install pm2 -g', shell=True)
subprocess.call('sudo pm2 startup', shell=True)
os.chdir(server)
subprocess.call('sudo pm2 start bin/www', shell=True)
subprocess.call('sudo pm2 start request.js', shell=True)
subprocess.call('sudo pm2 save', shell=True)
os.chdir(home)

print ('\nInstalling Hostapd & dnsmasq\n')
subprocess.call('sudo cp /home/pi/SettingBackup/dnsmasq.conf /etc/dnsmasq.conf', shell=True)
subprocess.call('sudo apt-get install -y hostapd dnsmasq', shell=True)

print ('\nPreconfig dnsmasq & hostapd\n')
subprocess.call('sudo chmod 602 /etc/wpa_supplicant/wpa_supplicant.conf', shell=True)
subprocess.call('sudo cp /home/pi/SettingBackup/dnsmasq.conf /etc/dnsmasq.conf', shell=True)
subprocess.call('sudo cp /home/pi/SettingBackup/hostapd.conf /etc/hostapd/hostapd.conf', shell=True)
subprocess.call('sudo cp /SettingBackup/defaultHostapd /etc/default/hostapd', shell=True)
subprocess.call('sudo cp /home/pi/SettingBackup/hostapd /etc/init.d/hostapd', shell=True)
subprocess.call('sudo sysctl -w net.ipv4.ip_forward=1', shell=True)
subprocess.call('sudo cp /home/pi/SettingBackup/interfaces1 /etc/network/interfaces1', shell=True)
subprocess.call('sudo cp /home/pi/SettingBackup/interfaces2 /etc/network/interfaces2', shell=True)
subprocess.call('sudo chmod 744 /home/pi/Public/NodeJS-Server/RFSniffer1', shell=True)
subprocess.call('sudo chmod 744 /home/pi/Public/NodeJS-Server/codesend', shell=True)
subprocess.call('sudo crontab /home/pi/SettingBackup/crontabBackup', shell=True)
subprocess.call('sudo cp /home/pi/SettingBackup/hosts /etc/hosts', shell=True)
subprocess.call('sudo hostnamectl set-hostname WirelessHome', shell=True)
subprocess.call('sudo python Public/NodeJS-Server/fileCheck.py', shell=True)
