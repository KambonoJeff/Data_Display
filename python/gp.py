import subprocess
import random
import string
import time
from datetime import datetime

cmd_command = " git add ."
cmd_command1 = " git commit -a -m \"python testing\" "
cmd_command2 = "git push -u origin"

current_time = datetime.now()

def deploy():
    
    completed_process = subprocess.run(cmd_command, shell=True, check=True, text=True)

    if completed_process:
        print("FIRST process completed")

        time = print("Current Time:\n",current_time.strftime("%Y-%m-%d %H:%M:%S") )
        time
        time
        time
        time
        time
        time
        time

    else:
        print(" FIRST NOT COMPLETED!!!!")
        
        time = print("Current Time:\n",current_time.strftime("%Y-%m-%d %H:%M:%S") )
        time
        time
        time
        time
        time
        time
        time

    completed_process1 = subprocess.run(cmd_command1, shell=True, check=True, text=True)
    
    if completed_process1:
        print("SECOND process completed")
        print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print(" SECOND NOT COMPLETED!!!!")
        print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))            
    completed_process2 = subprocess.run(cmd_command2, shell=True, check=True, text=True)
    if completed_process2:
        print("THIRD process completed")
        print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print(" THIRD NOT COMPLETED!!!!")
        print("Current Time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

    print("SUCCESSFULLY PUSHED ALL FILES :")
    exit()

def get_user_input():
    return input("ENTER THE NUMBER OF COMMITS: ")

def text_generator_a():
    with open("test.txt", "a") as file:
        random_string = ' '.join(random.choices(string.ascii_letters, k=20))
        file.write(random_string)
def text_generator_w():
    with open("test.txt", "w") as file:
        random_string = ' \n'.join(random.choices(string.ascii_letters, k=2000))
        file.write(random_string)

def randomFunc():
    option = [text_generator_a,text_generator_w]
    executeThis = random.choice(option)
    executeThis()

def formation():
    text_generator_w()
    deploy()

def rounds():
    userInput = get_user_input()
    try:
        number=int(userInput)
        ######################################

        ######################################
        print("THE USER INPUT IS :" , number)
        if number > 20:
            print("The number is greater than 20 enter less commits")
            get_user_input()

        min_time = 200
        max_time = 600
        sleep_time =random.randint(min_time,max_time)

        for _ in range(number):
            formation()
            time.sleep(sleep_time)

    except ValueError:
        print("NOT AN INTEGER!!!")


try:
    rounds()
    
   

except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code: {e.returncode}")
    print(f"Error message LEVEL 0NE ALERT : {e.stderr}")
