# //SSH
# Ausführen gleichen befehle über mehrere SSH-Sitzungen

import paramiko
import time
from pprint import pprint


hostnames = ["10.99.0.19", "10.99.0.44"]
commands = ['aaa radius-server local db-type ldap-server sub-type edirectory', 'save config']


def comments(inputs):
    print('------------------------------')
    print(inputs)
    print('------------------------------')


def parassh():
    comments("//SSH | V0.3 | Robert Schaller")
    username = input("Benutzername: ")
    passw = input("Paswort: ")

    for host in hostnames:
        comments("Running on: " + host)
        i = True
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=passw)

        channel = ssh.invoke_shell()
        channel_data = str(channel.recv(9999))

        while i:
            if channel.recv_ready():
                channel_data += str(channel.recv(9999))
                pprint(channel_data)
            else:
                continue

            for command in commands:
                print(command)
                channel.send(command+"\n")
                channel.send("")
                time.sleep(4)

            i = False

    print(host + " - Erledigt")
    ssh.close()


parassh()
