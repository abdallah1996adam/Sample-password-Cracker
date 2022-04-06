import pwd
import random
import pyautogui 

chars="abcefgdksgh1234567890"

allchars = list(chars)

pwd = pyautogui.password('plesase enter a password:')

sample_pwd = ""

while(sample_pwd != pwd):
    sample_pwd = random.choices(allchars, k=len(pwd))
    print("<====>" + str(sample_pwd) + "<======>")

    if(sample_pwd == list(pwd)):
        print("the password is : " + "".join(sample_pwd))
        break