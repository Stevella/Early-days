#! python3
#an insecure password locker program and incomplete program

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6','blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt','luggage': '12345'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("password for %s copied to clipboard" %(account))
else:
    print('%s not in the password manager' %(account))
    pw = input('Enter the password for %s:' %(account))
    PASSWORDS[account] = pw
    print('password for %s added' %(account))
    print(PASSWORDS)
