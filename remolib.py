import subprocess
import sys



class remossh(object):
   red = "\033[31m"
   blue = "\033[34m"
   bold = "\033[1m"
   reset = "\033[0m"
   green = "\033[32m"
   yellow = "\033[33m"

   def connect(host, cmd):


      ssh = subprocess.Popen(["ssh", "%s" % host, cmd],
         shell=False,
         stdout=subprocess.PIPE,
         stderr=subprocess.PIPE)

      result = ssh.stdout.readlines()
      if result != []:
         print(green + "[" + bold + " MESSAGE !\033[0m" + green + " ]")
         print(result)
         print("\n")
      else:
         print(red + "[" + bold + " NO RESPONSE !\033[0m" + red + " ]")