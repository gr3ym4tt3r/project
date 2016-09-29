#Automated Debugging??

Experimenting with WinAppDBG and Python. Eventually, I would like to automate it for exploit dev to find bad characters and/or jump addresses and the like. So far, this is just a project that I would like to push further. Until then, we shall see if it works. As of right now, output is like this:    

    PS C:\Users\IEUser\Desktop> python project.py
    [+] Searching for sipXezPhone.exe...
            [!] Unable to find sipXezPhone.exe
    [+] Starting sipXezPhone.exe
    [+] Searching for sipXezPhone.exe...
    [+] Found! sipXezPhone.exe has PID 2884
    [+] Attaching to sipXezPhone.exe
    PS C:\Users\IEUser\Desktop>

As of right now, here is what it does:    
1. Search for a hardcoded process. It'll eventually turn into an argument       
2. If it doesn't find it, it will start it    
3. It will search again and get the PID   
4. After finding, it will attach itself to the process
