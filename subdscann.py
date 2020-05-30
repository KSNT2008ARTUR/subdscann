from loguru import logger
import requests
import os,sys
import time

intro = """
           _         _                           
 ___ _   _| |__   __| |___  ___ __ _ _ __  _ __  
/ __| | | | '_ \ / _` / __|/ __/ _` | '_ \| '_ \ 
\__ \ |_| | |_) | (_| \__ \ (_| (_| | | | | | | |
|___/\__,_|_.__/ \__,_|___/\___\__,_|_| |_|_| |_|
|   |   |  |   |  |    |  | |   |  |   | | | | ||                 
|   |   |  |   |  |    |  | |   |  |   | | | | ||                     
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""" 
LR = '\033[1;31m' # light red
LG = '\033[1;32m' # light green
LO = '\033[1;33m' # light orange
LB = '\033[1;34m' # light blue
LP = '\033[1;35m' # light purple
LC = '\033[1;36m' # light cyan
@logger.catch   #CATCH ERROR with logger
def scanner(target): 
    #@logger.catch
    logger.debug("Started subdomain scann")
    logger.debug("reading file...")
    content = wordlist.read()
    logger.debug("Spliting wordlist....")
    #split by new lines
    subdomains = content.splitlines()
    for subdomain in subdomains:        #main loop
        full_path = f"http://{subdomain}.{target}"
        #URL construct
        timeout = 5
        totaltimeout = timeout + time.time()
        if time.time() > totaltimeout:
            logger.warning("Site is not responding")
        try: #trying connect to path
            requests.get(full_path)
            if time.time() > totaltimeout:
                logger.warning("Site is not responding")
        except requests.ConnectionError:
            if time.time() > totaltimeout:
                logger.warning("Site is not responding")
            logger.warning("Not found: " + full_path)
        logger.success("Found: " + full_path)
        if time.time() > totaltimeout:
                logger.warning("Site is not responding")
    logger.info("Scann ended.")
print(LO+intro) #intro
print(LR+"=======================Maded by root.kalihacker===============================")
print("                                                                              ")
logger.debug("subdscann started, reading wordlist...")
try:
    wordlist = open("wordlist.txt")
except Exception:
    logger.error("Not found wordlist please check wordlist.txt file!")
    logger.critical("Exiting!")
    sys.exit(1)
logger.success("Wordlist loaded")

question = logger.level(name="QUESTION", no=38, color = "<yellow>", icon="")
logger.log("QUESTION","Enter the target: ")
target = input(": ")
#print("                                                                                 1             2" )
#logger.log("QUESTION","Type the protocol [http://] or [https://] ")
#protocol = input(": ")
logger.log("QUESTION", "do you want to save scan results? ")
savq = input("[ y / n ]: ")
if savq == "y":
    SaveResults = True
    logger.debug("Creating file...")
    logger.add("file_{time}_subdomains.-{target}log")
    logger.success("File created!")
else:
    SaveResults = False


logger.debug("Trying conection to target...")
response = os.system("ping -c 1 " + target)
if response == 0:
    logger.success("Connected to target OK!")

    scanner(target)
    sys.exit(0)
else:
    logger.warning("timed out site is not responding try again...")
    logger.debug("re-Trying conection to target...")
response = os.system("ping -c 1 " + target)
if response == 0:
    logger.success("Connected to target OK!")
    scanner(target)
    sys.exit(0)
else:
    logger.critical("site is not responding! exiting!")
