#!/usr/bin/env python3
import sys
import socket
def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True
def main():
    print("hai")
    ip=input("Enter an ip address")
    print('ip4:',is_valid_ipv4_address(ip))
    print('ip6:',is_valid_ipv6_address(ip))

if __name__ == '__main__':
    main()
