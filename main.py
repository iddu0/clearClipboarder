######################
# Imports
######################

import pyperclip # Used for copying, and pasting
import argparse # Used for the arguments (-p, -c)

######################
# Variables
######################

# Creates a parser object that handels arguments (-p, -c)
par = argparse.ArgumentParser(description="clearClipboarder")

# The copy-to-clipboard argument
par.add_argument('-c', '--copy', action='store_true', help='Copy something to the clipboard')
# The paste-clipboard argument
par.add_argument('-p', '--paste', action='store_true', help='Paste the contents of the clipboard')

# Variable to simplify typing
args = par.parse_args()

######################
# Main Script
######################

# If using the -p argument, paste the contents of the clipboard into the console
if args.paste: 
    # Prints the users copied text into the console
    print(pyperclip.paste()) 
# If using the -c argument, copy the users console input
if args.copy: 
    # The users input to copy
    copyinput = input("Text to copy: ") 
    # Copying the users input into their clipboard
    pyperclip.copy(copyinput) 
    # Printing the confirmation of the text being copied
    print("Copied!") 

# Copy nothing only if not copying or pasting text
if not args.copy and not args.paste:
    pyperclip.copy('')  # Only clear clipboard if no flags passed
