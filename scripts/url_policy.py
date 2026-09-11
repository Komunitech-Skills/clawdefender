#!/usr/bin/env python3
"""URL preflight only; the HTTP transport must recheck redirects/resolved peers."""
import ipaddress
import socket
import sys
from urllib.parse import urlsplit


def check(url):
    parsed=urlsplit(url)
    if parsed.scheme not in ('https','http') or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError('HTTP(S) URL without userinfo required')
    host=parsed.hostname.rstrip('.').lower()
    if host=='localhost' or host.endswith(('.localhost','.local','.internal')):raise ValueError('private host')
    try:addresses=[ipaddress.ip_address(host)]
    except ValueError:
        addresses=[ipaddress.ip_address(x[4][0]) for x in socket.getaddrinfo(host,parsed.port or 443,type=socket.SOCK_STREAM)]
    if not addresses or any(not ip.is_global or (getattr(ip,'ipv4_mapped',None) and not ip.ipv4_mapped.is_global) for ip in addresses):
        raise ValueError('non-public resolved address')


if __name__=='__main__':
    try:check(sys.argv[1]);print('URL preflight passed; transport must enforce address and redirect policy')
    except (ValueError,OSError,IndexError):print('URL blocked or resolution unavailable',file=sys.stderr);sys.exit(1)
