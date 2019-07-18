#1 SURVEY
import json
def takesurvey(q_list , a_list):
  answer = {} #DICTIONARY FOR ANSWERS
  for q in q_list: #FOR EVERY QUESTION IN THE LIST OF QUESIONS
    answer[q] = input(q) #ASK EVERY QUESTIONS
  a_list.append(answer)

a = [] #LIST OF ANSWERS

q= ["What is your name? ","What is your favorite movie? ","How old are you? ","What is your favorite color? ","What school do you go to? ","What is your favorite drink "]

for i in range(5):
  takesurvey(q,a)
print(a)
#poop
