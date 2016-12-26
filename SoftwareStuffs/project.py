from sys import argv, exit
import pefile
try:
    from keystone import *
    from capstone import *
except ImportError as error:
    print('[!] Uh-oh: {}. Please install'.format(error))
    if 'keystone' in str(error):
        print('[!] pip install keystone-engine')
        exit()
    else:
        print('[!] pip install capstone')
        exit()

def assemblyInstructions(firstSet, imageBase):
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    print('\n[+] First few instructions:')
    for (address, size, mnemonic, op_str) in md.disasm_lite(firstSet, imageBase):
        print('\t{:08x}: {} {}'.format(address, mnemonic, op_str))

def main(application):
    pe = pefile.PE(application)
    IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE  = 0x40
    entrypoint = pe.OPTIONAL_HEADER.AddressOfEntryPoint
    firstSet = pe.get_memory_mapped_image()[entrypoint: entrypoint + 24]
    imageBase = entrypoint + pe.OPTIONAL_HEADER.ImageBase

    print('[+] Gathering information for {}...\n'.format(application))
    if (pe.OPTIONAL_HEADER.DllCharacteristics & IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE):
    	print('[!] ASLR is enabled. One moment...')
	    pe.OPTIONAL_HEADER.DllCharacteristics &= ~IMAGE_DLL_CHARACTERISTICS_DYNAMIC_BASE
	    print('[+] ASLR is now disabled!')
    else:
	    print('[+] ASLR is not enabled!')
    print('[+] Entry point: {:08x}'.format(imageBase))

    print('[+] Contains the following {} sections:'.format(pe.FILE_HEADER.NumberOfSections))
    for section in pe.sections:
	    print('\t{}: {:08x} \t{:08x} \t{:08x}'.format(
            section.Name,
		    section.VirtualAddress, 
		    section.Misc_VirtualSize, 
		    section.SizeOfRawData))
            
    assemblyInstructions(firstSet, imageBase)

if __name__ == '__main__':
    print('[+] Doing stuffs to stuggs because stuffs')
    try:
        application = argv[1]
    except IndexError as error:
        print('[!] Uh-oh: Usage {} [ application ]'.format(argv[0]))
        exit()
    main(application)
