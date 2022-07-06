import platform    # For getting the operating system name
import subprocess  # For executing a shell command
from time import sleep
host="recreation.gov"
def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    net_stat=subprocess.call(command) == 0
    if net_stat==True:
        print("Network Alive, continuing")
        Test()
    else:
        print("Network Down, waiting")
        Fail()
    return net_stat

def Test():
    print("Within test")

def Fail():
    print("Within Fail")
    sleep(10)
    ping(host)

ping(host)