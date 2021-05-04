import os,sys,time
from time import sleep

#Warna
r = '\033[1;31m'
g = '\033[1;32m'
y = '\033[1;33m'
b = '\033[1;34m'
p = '\033[1;35m'
c = '\033[1;36m'
w = '\033[1;37m'

def loop():
    print(f'  {w}|')
    print(f'  {w}|---------> {c}Ingin beli yang lain? {w}[{g}y{w}/{r}t{w}]')
    print(f'  {w}|')
    loop = input(' [+]------------> ')
    if(loop=="y"):
      time.sleep(2)
      menuu()
    elif(loop=="t"):
      print('  |')
      print(f' [+]  {g}Jangan lupa datang kembali ke Emwemart :)')
      time.sleep(2)
      os.system('exit')
    else:
      print(f' {w}[!] {r}Mesin Error : {c}Pilih yang bener!!')
      time.sleep(2)
      loop()

def banner():
    os.system('clear')
    print(f' {w}[+]----------------- {c}Selamat Datang Di Emwemart {w}-----------------[+]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Menu')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Info')
    print(f'  {w}|')
    print(f'  {w}|-----> {r}Exit')
    print(f'  {w}|')
    print(f'  {w}|--------> {y}Masukan pilihan anda ({r}Note{y}: gunakan huruf kecil saja{w}) : ')
    print(f'  {w}|')
    menu = input(' [+]-----------> ')
    if(menu=="menu"):
      menuu()
    elif(menu=="info"):
      infoo()
    elif(menu=="exit"):
      print(f' {y}Jangan lupa datang kembali ke Emwemart :)')
      time.sleep(2)
      os.system('exit')
    else:
      print(f'{w} [!] {r}Mesin eror : {c}Pilih yang bener!!')
      time.sleep(2)
      banner()

def menuu():
    os.system('clear')
    print(f' {w}[+]---------------------------- {c}Menu{w} ----------------------------[+]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Lays              {g}[Rp 11.400]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Chitato           {g}[Rp 11.800]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Doritos           {g}[Rp 12.000]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Potabea           {g}[Rp  8.300]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Taro              {g}[Rp  7.700]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Softex            {g}[Rp 33.400]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Biore             {g}[Rp 27.200]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Lifeboy           {g}[Rp 32.600]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Dettol            {g}[Rp 42.500]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Teh Botol         {g}[Rp  5.300]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Teh Pucuk         {g}[Rp  5.200]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Fruit Tea         {g}[Rp  6.400]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Yakult            {g}[Rp  9.000]')
    print(f'  {w}|')
    print(f'  {w}|-----> {c}Ultramilk         {g}[Rp  7.800]')
    print(f'  {w}|')
    print(f'  {w}|')
    pil = input('  |---------> Pilih barang : ')
    if(pil=="lays"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Lays sebanyak {w}[{jum}]{g} dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*11400,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*11400,']')
      loop()
    elif(pil=="chitato"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Chitato sebanyak{w} [{jum}]{g} dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*11800,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*11800,']')
      loop()
    elif(pil=="doritos"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Chitato sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*12000,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*12000,']')
      loop()
    elif(pil=="potabea"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Potabea sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*8300,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*8300,']')
      loop()
    elif(pil=="taro"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Taro sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*7700,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*7700,']')
    elif(pil=="softex"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Softex sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*33400,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*33400,']')
      loop()
    elif(pil=="biore"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Biore sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*27200,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*27200,']')
      loop()
    elif(pil=="lifeboy"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Lifeboy sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*32600,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*32600,']')
      loop()
    elif(pil=="dettol"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Dettol sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*42500,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*42500,']')
      loop()
    elif(pil=="teh botol"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Teh Botol sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*5300,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*5300,']')
      loop()
    elif(pil=="teh pucuk"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Teh Pucuk sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*5200,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*5200,']')
      loop()
    elif(pil=="fruit tea"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Fruit Tea sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*6400,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*6400,']')
      loop()
    elif(pil=="yakult"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Yakult sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*9000,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*9000,']')
      loop()
    elif(pil=="ultra milk"):
      jum = int(input('  |---------> Berapa jumlah barang : '))
      bay = int(input('  |---------> Berapa pembayaran kamu : '))
      print('  |')
      print(f'  |  {g}Kamu membeli Ultra Milk sebanyak {w}[{jum}] {g}dengan uang {w}[{bay}]')
      print(f'  |  {y}Total : {w}[',jum*7800,']')
      print(f'  |  {y}Jadi kembaliannya : {w}[',bay-jum*7800,']')
      loop()
    else:
      print(f'  |  {w}[!] {r}Mesin Error : {c}Nama produk yang anda masukan tidak ada!!')
      time.sleep(2)
      menuu()

def loopinfo():
    print(f'  {w}|')
    print(f'  {w}|-------> {b}Back? {w}[{g}y{w}/{r}t{w}]')
    print(f'  {w}|')
    tanya = input(' [=]------------> ')
    if(tanya=="y"):
      time.sleep(1)
      banner()
    elif(tanya=="t"):
      infoo()
    else:
      print(f' {w}[!] {r}Mesin Error : {c}Pilih yang benar!!')
      time.sleep(2)
      infoo()

def infoo():
    os.system('clear')
    print(f' {w}[=]---------------------------- {c}Info{w} ----------------------------[=]')
    print(f'  {w}|')
    print(f'  {w}|-----> {y}Pemilik     : {w}EmweCyber')
    print(f'  {w}|')
    print(f'  {w}|-----> {y}Negara      : {r}Indo{w}nesia')
    print(f'  {w}|')
    print(f'  {w}|-----> {y}Kota        : {r}Parung {w}Panjang')
    print(f'  {w}|')
    print(f'  {w}|-----> {y}Code Script : {p}Python')
    print(f'  {w}|')
    print(f'  {w}|')
    print(f'  {w}|  {c}Script ini dibuat sendiri oleh seorang yang bisa di katakan')
    print(f'  {w}|  {c}profesional dalam bahasa {p}Python{c}, walau pemilik script ini hanya')
    print(f'  {w}|  {c}bisa bahasa {p}Python {c}dan {w}Shell {c}tapi baginya itu sudah cukup untuk')
    print(f'  {w}|  {c}menyenangkan hobby codingnya')
    print(f'  {w}|  {c}Sekian info untuk script kasir ini, Terima Kasih :)')
    print(f'  {w}|  {w}~EmweCyber')
    loopinfo()

if __name__=="__main__":
    banner()
