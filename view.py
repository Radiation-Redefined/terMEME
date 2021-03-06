import subprocess
import sys
import time

from clint.textui import colored
from banner import *
from scrape import *


def main():
    
    # Clear up the terminal screen
    subprocess.call("clear", shell=True)
    print(banner())
    print()
    sub = check_validity()

    # Category menu
    print (colored.green("""[+] Wubba Lubba dub-dub!

    Select a Category:
    1) Top
    2) New
    3) Hot
    4) Rising
    5) Exit
    """))

    # Loop until valid category is selected
    while(True):
        
        ch = int(input(colored.green("Enter your choice: ")))
        print()
        if ch==1 or ch==2 or ch==3 or ch==4 or ch==5:
            if ch==5:
                sys.exit()
            else:
                break
            
        else:
            print(colored.red("[-] Invalid input detected please enter a valid input!"))
            print()

    # Fetch the image url based on the user set parameters and display them        
    if ch==1:
        print(colored.green("[+] Fetching the top images from r/{}....".format(sub)))
        print()  
        time.sleep(1)
        result = get_img(sub, "top")
        # Used an if else in all cases to check whether result is false or has the list
        if not result:
            sys.exit(1)
        else: 
            display(result)

    elif ch==2:
        print(colored.green("[+] Fetching the new images from r/{}....".format(sub)))
        print()
        time.sleep(1)
        result = get_img(sub, "new")
        if not result:
            sys.exit(1)
        else: 
            display(result)

    elif ch==3:
        print(colored.green("[+] Fetching the hot images from r/{}....".format(sub)))
        print()
        time.sleep(1)
        result = get_img(sub, "hot")
        if not result:
            sys.exit(1)
        else: 
            display(result)

    elif ch==4:
        print(colored.green("[+] Fetching the rising images from r/{}....".format(sub)))
        print()
        time.sleep(1)
        result = get_img(sub, "rising")
        if not result:
            sys.exit(1)
        else: 
            display(result)
    

if __name__=="__main__": 
    main() 
