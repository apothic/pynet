import paramiko
import time
from getpass import getpass

ip_addr = '192.168.1.1'
username = 'cisco'
password = getpass()
port = 22
ssh_conn = paramiko.SSHClient()
ssh_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_conn.connect(ip_addr, username=username, password=password, port=port)
ssh_conn = ssh_conn.invoke_shell()

output = ssh_conn.recv(5000)
ssh_conn.send("ping 8.8.8.8\n")
time.sleep(5)
output = ssh_conn.recv(5000)

print output
