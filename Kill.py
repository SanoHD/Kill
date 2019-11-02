import sys, os
try: file = open(sys.argv[1])
except: print("[KILL] Invalid file!"); sys.exit()
fr = file.read().strip()
file.close()
if fr == "!": os.remove(sys.argv[1])
else: print("[KILL] Invalid command!"); sys.exit()
"""To make the interpreter bigger, i decided to create a story...
A long time ago, there was a man. Big, attractive, stupid.
Because of his stupidity, he build hisself a robot.
This robot killed the man, because robots are evil.
Like this "Programming Language".
Dont do drugs, kids."""
