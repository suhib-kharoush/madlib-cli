from os import replace
import re
import random
from typing import Text

def welcome_message():
    print("Welcome to Madlib game, ready to start? 😃")

def instructions():
    print("""
    I will ask you some questions,\n then you will guess the answer, \n after that when you finish, I will show you the results \U0001F600 
    """)

welcome_message() 
instructions()

def read_template(p):
    with open(p, 'r') as file:
      template = file.read().strip("\n")

    return template



def parse_template(text):
    parts = []
    parts = re.findall(r'\{.*?\}', text)
    for i in range(len(parts)):
         parts[i] = parts[i].replace("{", "")
         parts[i] = parts[i].replace("}", "")

    for i in range(text.count("{")):
          text = text.replace(parts[i], "")

    part_template = ()
    for i in parts:
        part_template = part_template + (i,)
    # print(text)
    # print(part_template)
    return text, part_template 

parse_template("It was a {Adjective} and {Adjective} {Noun}.")



def merge(text, parts):
    return text.format(*parts)

merge("It was a {} and {}.", ("dark", "stormy", "night"))


def new_file(result):
     n = random.random()
     with open("assets/f{}.txt".format(str(n)), 'w') as file:
         file.write(result)
     print(merge("It was a {} and {} {}.", ("dark", "stormy", "night")))

def get_data():
    text = read_template("assets/make_me_a_video_game_template.txt")
    originalText = read_template("assets/make_me_a_video_game_output.txt")
    stripped_text, parts_tuple = parse_template(text)
    answers = []

    for i in range(len(parts_tuple)):
        x = input("enter a {} >".format(parts_tuple[i]))
        answers.append(x)
    results = stripped_text.format(*answers)
    print(results)
    new_file(results)
    print(originalText)



    
if __name__ == '__main__':
  get_data()
