import subprocess
import os


home = '/home/pi'
server = 'Public/NodeJS-Server'

print("Install Ansible")
subprocess.call("apt update -y", shell=True)
subprocess.call("apt-get install -y ansible", shell=True)

print("Running ansible playbook")
subprocess.call(["ansible-playbook", "setup.yml", "-vv"])
