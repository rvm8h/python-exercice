import subprocess
import os

#connection à distance au serveur
subprocess.call("ssh-keygen -t rsa")
subprocess.call("ssh-copy-id bibi@<VM IP address>")
subprocess.call("ssh bibi@<VM IP address>")
subprocess.call('bibi_mdp')

#installation diverses
subprocess.call('yum -y install net-tools')
subprocess.call('yum -y update')
if os.popen('rpm -qa kernel |sort -V |tail -n 1').read() != os.popen('uname -r').read(): os.popen('reboot')
subprocess.call("sudo yum -y install lsof")
subprocess.call("sudo yum -y install elinks")

#installation de git
subprocess.call('sudo yum -y install git')

print(os.popen("git --version").read())


#git clone
subprocess.call("git clone git clone https://github.com/rvm8h/python-exercice.git")
subprocess.call("cd /python-exercice")
subprocess.call("git checkout branch -b Olivier")

#installation de python
subprocess.call("sudo yum -y install yum-utils")
subprocess.call("sudo yum -y groupinstall development")
subprocess.call("sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm")
subprocess.call("sudo yum -y install python36u")
print(subprocess.call("python3.6 -V"))


#installation de pip
subprocess.call("sudo yum -y install python36u-pip")

#installation de flask
subprocess.call("sudo pip3.6 install flask")

#ouverture du firewall
subprocess.call("sudo firewall-cmd --zone=public --add-port=<Port à ouvrir>/tcp")

#lancement du serveur
subprocess.call("python3.6 web_flask_OT runserver")
print(subprocess.call("lsof -i :<Port ouvert>"))
subprocess.call("elinks <VM IP address>:<Port ouvert>")



