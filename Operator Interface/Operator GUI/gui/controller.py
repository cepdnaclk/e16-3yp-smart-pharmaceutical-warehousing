import subprocess
import os
import signal
import time

Code = "cd ..; cd ..; python3 GUI.py"
streamTerminal = None

def run():
    global streamTerminal
    streamTerminal = subprocess.Popen(Code,shell = True, preexec_fn=os.setsid)

def kill():
    global streamTerminal
    os.killpg(os.getpgid(streamTerminal.pid), signal.SIGTERM)

# run()
# time.sleep(100)
# kill()