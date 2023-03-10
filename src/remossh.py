import itertools
import threading
import time
import sys
import subprocess
from halo import Halo

session0 = False

red = "\033[31m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"
green = "\033[32m"
yellow = "\033[33m"
colors = [
   "\033[38;5;226m",
   "\033[38;5;227m",
   "\033[38;5;229m",
   "\033[38;5;230m",
   "\033[38;5;190m",
   "\033[38;5;191m",
   "\033[38;5;220m",
   "\033[38;5;221m",
   "\033[38;5;142m",
   "\033[38;5;214m",
]



#here is the animation


spinner = Halo(text='Starting the remossh console', spinner='dots')
spinner.start()

time.sleep(3)

spinner.stop()

print(f"""

{red} (           *        )   (    (        )  {bold}
{red} )\ )      (  `    ( /(   )\ ) )\ )  ( /(  {bold}
{red}(()/( (    )\))(   )\()) (()/((()/(  )\()) {bold}
{red} /(_)))\  ((_)()\ ((_)\   /(_))/(_)) ((_)\  {bold}
{red}(_)) ((_) (_()((_)  ((_) (_)) (_))   _((_) {bold}
{blue}| _ \| __||  \/  | / _ \ / __|/ __| | || | {bold}
{blue}|   /| _| | |\/| || (_) |\__ \\__ \ | __ | {bold}
{blue}|_|_\|___||_|  |_| \___/ |___/|___/ |_||_| {bold}
                                           

""")


command = input(blue + "remossh" + bold + "\033[0m > \033[0m")

rhost = None

if "connect" in command:
   HOST = input(blue + "remossh" + bold + "(host) > \033[0m")
   print(yellow + "[" + bold + " You can only enter 1000 commands for this session. \033[0m" + yellow + " ]")

   for i in range(1000):
      COMMAND = input(blue + "remossh" + bold + "(session) > \033[0m")

      try:
         if "exit" in COMMAND:
            print(yellow + "[" + bold + " SESSION CUT SHORT! \033[0m" + yellow + " ]")
            sys.exit(0)

         ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)

         result = ssh.stdout.readlines()
         if result != []:
            print(green + "[" + bold + " MESSAGE FROM HOST !\033[0m" + green + " ]")
            print(result)
            print("\n")
         else:
            print(red + "[" + bold + " NO RESPONSE !\033[0m" + red + " ]")

      except Exception as e:
         error = ssh.stderr.readlines()
         print(sys.stderr, "ERROR: %s" % error)



else:
   print(red + "[" + bold + " COMMAND NOT FOUND !\033[0m" + red + " ]")
