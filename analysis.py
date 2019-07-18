import json
f= open("survey.json","r")
x = json.load(f)
f.close()

sum_ages = 0
lst_ages =[]
for i in x:
    temp = i["How many siblings do you have? "]
    if temp.isnumeric():
        age = int(temp)
        sum_ages += age
        lst_ages.append(age)
avg = sum_ages / len(x)
print(avg)
print(lst_ages)
