##Python3
#login.py
#larry li coliguanda@gmail.com

import fileinput
import hashlib
from types import*
print("plz log in")
MAX_TRY = 5
PASSWORD = 'b8d466499686cb3b80b06ce81229c7ac'
count = 0
def encry (password_str):

    password_md5 = hashlib.md5(password_str.encode('utf-8')).hexdigest()
    return password_md5



while count <= MAX_TRY:
          usr_choice =input("Type 'q' to exit this program or type 'y' continue")
          if usr_choice == 'q':
              break
          if usr_choice == 'y':
             print('got here!')
             password = input ('Type your password')
             if isinstance(password,str):
                 if PASSWORD == encry(password):
                     print('LOGIN!!!!')
                     break
                 else:
                     print('Wrong password, retry! remining :' ,MAX_TRY - count , " times ")
                     count = count + 1
             else:
                 print('Password is in wrong data type, we only accept str')

          else:
              print('Invalid input')

if count >5:
    print('Exceed MAX')
