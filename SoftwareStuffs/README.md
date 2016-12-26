# Just experimenting with stuff

A few things I am experimenting with. Getting information of a file and instructions and what not  
    
Output:    

    X:\Project\PythonProjects>python project.py
    [+] Just another project!
    [!] Uh-oh: Usage project.py [ application ]
    
    X:\Project\PythonProjects>python project.py putty.exe
    [+] Just another project!
    [+] Gathering information for putty.exe...

    [+] ASLR is not enabled!
    [+] Entry point: 004550f0
    [+] Contains the following 4 sections:
            .text   : 00001000      0005bf81        0005c000
            .rdata  : 0005d000      0001d47a        0001e000
            .data   : 0007b000      00005944        00002000
            .rsrc   : 00081000      00002ec0        00003000

    [+] First few instructions:
            004550f0: push 0x60
            004550f2: push 0x478108
            004550f7: call 0x457204
            004550fc: mov edi, 0x94
            00455101: mov eax, edi
            00455103: call 0x454bc0
            
This is a work in progress 
