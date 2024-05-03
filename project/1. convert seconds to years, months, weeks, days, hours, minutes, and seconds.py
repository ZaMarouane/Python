#Projecte

'''int_seconds = int ( input ( "Type how many seconds you want to convert:\n" ))

years = int_seconds // 31536000
remaining_seconds = int_seconds % 31536000
months = remaining_seconds // 2592000
remaining_secondsm = remaining_seconds % 2592000
weeks = remaining_secondsm // 604800
remaining_secondsw = remaining_secondsm % 604800
days = remaining_secondsw // 86000
remaining_secondsd = remaining_secondsw % 86000
hours = remaining_secondsd // 3600
remining_secondsh = remaining_secondsd % 3600
minutes = remining_secondsh // 60
remaining_secondsmi =  remining_secondsh % 60
seconds = remaining_secondsmi

print ( f"The number of years is {years}, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds")
'''

name = input ( "Enter your name:\n" )
#print(name.capitalize())
print (name + 5 )
