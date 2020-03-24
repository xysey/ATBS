#! python3

# pw.py an insecure password manager

PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345",
}

import sys, pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy the account password")
    sys.exit()

account = sys.argv[1]

if account not in PASSWORDS:
    print("There is no such account existing in my memory")
    sys.exit()
else:
    pyperclip.copy(PASSWORDS[account])
