import random

#znaleźć sposób jak uwzględnić kilka zakresów

def gene():
    long = int(input('How long should have been password? '))
    number = input('Should password contain numbers? ')
    upper = input('Should password contain uppercase? ')
    special = input('Should password contain special characters? ')
    password = ''
    for i in range(long):
        if number.lower() == 'yes' and upper.lower() == 'yes' and special.lower() == 'yes':
            password+=chr(random.choice(range(33,127)))
        elif number.lower() == 'yes' and upper.lower() == 'yes' and special.lower() == 'no':
            password+=chr(random.choice(range(48,122)))
        elif number.lower() == 'yes' and upper.lower() == 'no' and special.lower() == 'no':
            password+=chr(random.choice(range(48,57) and range(97,122)))
        elif number.lower() == 'no' and upper.lower() == 'no' and special.lower() == 'yes':
            password+=chr(random.choice(range(33,47) and range(97, 127))) 
        elif number.lower() == 'no' and upper.lower() == 'yes' and special.lower() == 'yes':
            password+=chr(random.choice(range(33,127) and range(97,127)))             
        elif number.lower() == 'no' and upper.lower() == 'yes' and special.lower() == 'no':
            password+=chr(random.choice(range(65,122) and range(97,122)))        
        else:
            password+=chr(random.choice(range(99,122)))   

    return str(password)


print(gene())