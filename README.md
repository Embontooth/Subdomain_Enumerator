# Subdomain Enumeration

This is a Python script for subdomain enumeration. It checks common subdomains across multiple TLDs, makes HTTP requests to see if they are active, and resolves their IPv4 and IPv6 addresses. The script uses multithreading for faster execution.

## Features
- Checks a predefined list of subdomains (www, mail, ftp, api, etc.)
- Supports multiple top-level domains like com, org, net, io, ai, tech and more
- Resolves both A (IPv4) and AAAA (IPv6) DNS records
- Multi-threaded scanning with ThreadPoolExecutor
- Prints results in a table format

## Requirements
- Python 3.7+
- requests
- dnspython

Install dependencies with:
pip install requests dnspython
