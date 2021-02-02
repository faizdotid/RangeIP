#Do u want recode? no problem but dont forget the author

from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init
import requests
init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
fw = Fore.WHITE

def ran(ip):
  listip = []
  try:
    i = ip.split('.')
    for x in range(1, 256):
      ips = '{}.{}.{}.{}'.format(i[0], i[1], i[2], str(x))
      listip.append(ips)
      sv = open(xxx.split('.')[0]+'_ranged.txt', 'a')
      sv.write(ips+'\n')
      sv.close()
    with ThreadPoolExecutor(max_workers=50) as runer:
      runer.map(cek, listip)
  except:
    print(fr+'[+] Something wrong [+]')
    
def cek(ip):
  if '://' not in ip: ip='http://'+ip
  else: pass
  try:
    cek = requests.get(ip, headers={'User-Agent': 'Mozzila'}, proxies={}, timeout=7)
    if cek.status_code == 200:
      print(fg+'[+] Live IP > '+fw+ip+fg+' [+]')
      sv = open(xxx.split('.')[0]+'_live_ip.txt', 'a')
      sv.write(ip+'\n')
      sv.close()
  except:
    print(fr+'[-] Dead IP > '+fw+ip+fr+' [-]')

xxx = input('LIST ~# ')
l = open(xxx, 'r').read().split('\n')
with ThreadPoolExecutor(max_workers=15) as run:
  run.map(ran, l)
