import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def checkPassword(password):
  if password == 'happychance':
    return True
  else:
    print('That password is incorrect')
    sys.exit(0)
    return False
def decodeFlagEnc(flagEnc):
  return decodeText(flagEnc.decode(), 'rapscallion')
def getPassword():
  return input('Please enter correct password for flag:')
def readFlagEnc():
  return open('flag.txt.enc', 'rb').read()
def printFlagLabel():
  print('Welcome back... your flag, user:')
def decodeText(password, flagDec):
    arg433 = flagDec
    i = 0
    while len(arg433) < len(password):
        arg433 = arg433 + flagDec[i]
        i = (i + 1) % len(flagDec)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(password,arg433)])
flagEnc = readFlagEnc()
password = getPassword()
checkPassword(password)
printFlagLabel()
flagDec = decodeFlagEnc(flagEnc)
print(flagDec)
sys.exit(0)

