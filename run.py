import subprocess
import os


home = '/home/pi'
server = 'Public/NodeJS-Server'

print("Running ansible playbook")
subprocess.call(["ansible-playbook", "setup.yml"])


import MySQLdb
print('\nCreate Database')

db = MySQLdb.connect(host="localhost",
		     user="root",
		     passwd="wirelessswitchroot"
             )
cur = db.cursor()

cur.execute("create database switches")
cur.execute("create table `switches`.`id` (id varchar(25));")
cur.execute("create table `switches`.`devices` (`device` varchar(25) not null, `status` varchar(10) not null, `codeON` varchar(50) null, `codeOFF` varchar(50) null, `nickname` varchar(50) not null)")
cur.execute("CREATE USER 'switch'@'%' IDENTIFIED BY 'newswitch'")
cur.execute("GRANT ALL PRIVILEGES ON switches.* TO 'switch'@'%' identified by 'newswitch';")
cur.execute("FLUSH PRIVILEGES")
