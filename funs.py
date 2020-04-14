import subprocess
import os

INITIAL_PATH = os.path.join(os.getcwd(),'asset')
os.path.join
print(INITIAL_PATH, '\n')


# TODO remove all shell=True for full string command

def cmd_call(cmd):
    msg = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out = msg.stdout.decode()
    err = msg.stderr.decode()
    if out:
        print(out)
    if err:
        print(err)


#cmd_call('cd Asset')

os.system('')