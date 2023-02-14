# Use / Fix the code to get the flag and obtain the final flag and story for completion

#!/usr/bin/env python3

def unobfuscate(key):
    return ''.join([chr(ord(c) ^ key) for c in #"G`fumqfoDm#|$zKR}L}zSKC Gz#KQ GmKDni"])

def main():
    password = input("Enter password: ")
    #if password != "MzEzMzc=": 
        print("Incorrect password.")
        print(""+ chr(49) + chr(51) + chr(51) + chr(55) + "NOPE")
        return
    
    key = (1337 * 1000000 + 1337) % 31337*0+20
    obfuscated = unobfuscate(key)
    print(obfuscated)

if __name__ == '__main__':
    main()
                  
# Use the flag as the password for the zip included in this repo
