from winappdbg import System, Debug
from re import compile

file = 'C:\\Users\\IEUser\\Desktop\\sipXezPhone-0.35a\\sipXezPhone.exe'

system = System()
debug = Debug()

def checkProcesses():
    for process in system:
        filename = process.get_filename()
        pid = process.get_pid()
        if file == filename:
            return pid

def cleanFilename(file):
    clean = compile(r'(?<=\\)\w+.exe')
    return clean.search(file).group()

if __name__ == '__main__':
    while True:
        name = cleanFilename(file)
        print('[+] Searching for {}...'.format(name))
        if checkProcesses() == None:
            print('\t[!] Unable to find {}'.format(name))
            print('[+] Starting {}'.format(name))
            system.start_process(file)
        else:
        	pid = checkProcesses()
        	print('[+] Found! {} has PID {}'.format(name, pid))
        	print('[+] Attaching to {}'.format(name))
        	debug.attach(pid)
        	break
