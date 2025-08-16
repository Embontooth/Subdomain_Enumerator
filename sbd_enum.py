import requests
from concurrent.futures import ThreadPoolExecutor
import dns.resolver

resolver = dns.resolver.Resolver()
domain = input("Enter your domain (Ex: youtube) : ")

subdomain = ["www","mail","ftp","blog","api","dev","test","shop","support","docs","m","news","secure"]
tld = ["com","org","net","info","biz","xyz","online","in","us","uk","au","ca","de","jp","fr","app","dev","io","ai","me","tech","store","cloud"]

ipv4 = []
ipv6=[]
discovered_subdomains = []

def check_subdomain(s,t):
    url = f'http://{s}.{domain}.{t}'
    try:
        requests.get(url,timeout=3)
    except requests.ConnectionError:
        return
    except requests.Timeout:
        return
    else:
        fd = f"{s}.{domain}.{t}" 
        try:
            v4 = [str(rdata) for rdata in resolver.resolve(fd, "A")]
        except dns.resolver.NoAnswer:
            v4 = []
        except dns.resolver.NXDOMAIN:
            v4 = []

        try:
            v6 = [str(rdata) for rdata in resolver.resolve(fd, "AAAA")]
        except dns.resolver.NoAnswer:
            v6 = []
        except dns.resolver.NXDOMAIN:
            v6 = []
        print(f'[+] Subdomain found {url}')
        discovered_subdomains.append(url)
        ipv4.append(v4)
        ipv6.append(v6)

print("Scanning... Please wait")
with ThreadPoolExecutor(max_workers=10) as executor:
    for s in subdomain:
        for t in tld:
            executor.submit(check_subdomain,s,t)

print(f"{'Subdomain':<35}{'IPv4':<40}{'IPv6'}")
print("-" * 100)
for i in range(len(discovered_subdomains)):
    print(f"{discovered_subdomains[i]:<35}{', '.join(ipv4[i]) or 'N/A':<40}{', '.join(ipv6[i]) or 'N/A'}")