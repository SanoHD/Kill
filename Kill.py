import sys, os

try: file = open(sys.argv[1])
except: print("[KILL] Invalid file!"); sys.exit()
fr = file.read().strip()
file.close()
if fr == "!": os.remove(sys.argv[1])
else: print("[KILL] Invalid command!"); sys.exit()
   
