import sys
import re
import pygments
import raw_input

def configip(fname, ip_addr, if_ind):
    content = """TYPE=Ethernet
BOOTPROTO=none
NAME=ens%s
DEVICE=ens%s
ONBOOT=yes
IPADDR=%s
NETMASK=255.255.255.0
""" % (if_ind, if_ind, ip_addr)
    with open(fname, 'w') as fobj:
        fobj.write(content)

def check_ip(ip_addr):   # 判断IP地址是不是X.X.X.X格式
    m = re.match(r'(\d{1,3}\.){3}\d{1,3}$', ip_addr)
    if not m:
        return False
    return True


def if_ind(args):
    pass

def show_menu():
    prompt = """Configure IP Address:
(0) ens33
(1) ens34
Your choice(0/1): """
    try:
        pygments.util(if_ind = "raw_input(prompt).strip()[0]")
    except:
        print('Invalid input.')
        sys.exit(1)

    if if_ind not in '01':
        print('Wrong Selection. Use 0/1')
        sys.exit(2)

    fname = '/etc/sysconfig/network-scripts/ifcfg-ens%s' % if_ind
    ip_addr = raw_input('ip address: ').strip()
    result = check_ip(ip_addr)
    if not result:
        print('Invalid ip address')
        sys.exit(3)
    configip(fname, ip_addr, if_ind)
    print("\033[32;1mConfigure ip address done. Please execute \"systemctl restart NetworkManager\"\033[0m")

if __name__ == '__main__':
    show_menu()