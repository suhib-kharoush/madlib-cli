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
      template = file.read()
    return template

read_template('./assets/make_me_a_video_game_2.txt')

def puzzles():
    questions = ['Guess my name?','name an adjective in my personality?', 'another one?','my friend name?', 'thing in his personality?', 'we plan to...?', 'adjective in the pet?', 'thing we want to steal?']
    x = []
    for i in questions:
        question = input(i)
        x.append(question)
    return x

def merge(text, result):
    data = text
    answer = data.format(*result)
    print(answer)
    return answer

with open('./assets/madlib_result.txt', 'w') as file:
    file.write(merge(read_template('./assets/make_me_a_video_game_2.txt'), puzzles()))
import re
def parse_template(text):
    data = re.findall(r"\{(.*?)\}", read_template(text))
    return data
print(parse_template('./assets/make_me_a_video_game_2.txt'))






 