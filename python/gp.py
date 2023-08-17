import subprocess
import random
import string
import time
from datetime import datetime
import requests

cmd_command = " git add ."
cmd_command2 = "git push -u origin"

current_time = datetime.now()

def commit_m():

    python_testing = ' '.join(random.choices(string.ascii_letters, k=32))
    cmd_command1 = " git commit -a -m \"  " + python_testing + " \" "
    print(cmd_command1)
    return cmd_command1

def deploy():
    
    completed_process = subprocess.run(cmd_command, shell=True, check=True, text=True)

    if completed_process:
        print("FIRST process completed")

        time = print("Current Time:\n",current_time.strftime("%Y-%m-%d %H:%M:%S") )
        

    else:
        print(" FIRST NOT COMPLETED!!!!")
        
        time = print("Current Time:\n",current_time.strftime("%Y-%m-%d %H:%M:%S") )
        
    completed_process1 = subprocess.run(commit_m(), shell=True, check=True, text=True)
    
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

def get_user_input():
    return input("ENTER THE NUMBER OF COMMITS: ")

def text_generator_a():
    min_content = 500
    max_content = 3000
    content = random.randint(min_content,max_content)

    with open("test.txt", "a") as file:
        random_string = ' '.join(random.choices(string.ascii_letters, k=208))
        file.write(random_string)
def text_generator_w():
    min_content = 500
    max_content = 3000
    content = random.randint(min_content,max_content)
    with open("test.txt", "w") as file:
        random_string = ' \n'.join(random.choices(string.ascii_letters, k=content))
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
        min_time = 100
        max_time = 300
        sleep_time =random.randint(min_time,max_time)
        for _ in range(number):
            formation()
            time.sleep(sleep_time)
    except ValueError:
        print("NOT AN INTEGER!!!")
def call_process():
    url = "https://www.google.com/"  
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(data)
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

##########################################################################...underdef:



try:
    rounds()    
except subprocess.CalledProcessError as e:
    print(f"Command failed with exit code: {e.returncode}")
    print(f"Error message LEVEL 0NE ALERT : {e.stderr}")
