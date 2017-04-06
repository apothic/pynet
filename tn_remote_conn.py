#!/usr/bin/env python
#Script in dev for send commands to multiple switches at once through Telnet.

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(6)
    return remote_conn.read_very_eager()

def login(remote_conn, username, password):
    output = remote_conn.read_until("ername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("ssword", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def main():
    
    ip_addrs = ['172.16.1.78','172.16.1.79','172.16.1.80','172.16.1.81'] 
    for ip_addr in ip_addrs:
        remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
        username = 'cisco'
        password = 'cisco'
        output = login(remote_conn, username, password)
        output = send_command(remote_conn, 'terminal length 0')
        output = send_command(remote_conn, 'sh ip int br')    
        print output

if __name__ == "__main__":
    main()
