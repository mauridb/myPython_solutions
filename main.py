#UTILITIES
import os,sys
from datetime import datetime
import csv
from models.User import User,Platform
from utilities.utility import search_num_lines
from termcolor import colored
# print dir(User)

# SETTINGS
from settings import setup
from settings import search_value_in_settings as srcs
settings = setup()
p = Platform()
p.setName('UndefinedTMM')
# print p.get_name()



# MAIN APPLICATION

if srcs(settings, 'YES'):
  # print 'inside first if'
  if srcs(settings, 'UndefinedTMM'): 
    #print len(p.users)
    u=p.sign_up(raw_input('Type your username:\n'),raw_input('Type your email address:\n'))
    # print p.users
    


    # csv operation:
    #   - calc how many line in csv
    #   - write 
     
    fieldnames= [
        'ID',  
        'USERNAME',  
        'EMAIL',  
        'PASSWORD',  
        'FIRST_NAME',  
        'LAST_NAME',  
        'DATE_REGISTRATION',  
        'TIMES_LOGGED_IN',  
    ]

    if settings['database'] not in os.listdir('.'):
      with open(settings['database'], 'w') as myFile:
        writer = csv.DictWriter(myFile, fieldnames=fieldnames)
        writer.writeheader()

    print colored('##############\nSUCCESS\n############', 'blue')
    
    with open(settings['database'],'a') as myFile:
      writer = csv.DictWriter(myFile, fieldnames=fieldnames)
      writer.writerow({
          'ID':search_num_lines(settings['database']),
          'USERNAME':u.username,
          'EMAIL':u.email,
          'PASSWORD':u.password,
          'FIRST_NAME':' null ',
          'LAST_NAME':' null ',
          'DATE_REGISTRATION':u.date_join,
          'TIMES_LOGGED_IN':0,
      })
# print 'lines in csv'      
# print colored(search_num_lines(settings['database']),'red')
print 'Ok see you soon..'
