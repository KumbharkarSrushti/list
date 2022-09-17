import requests
import json
import os.path
if os.path.exists("new.json"):
    print("file exist")
    d=open("new.json","r")
    file=d.read()
    data=json.loads(file)
else:
    print("file not exist")
    URL=requests.get("https://api.merakilearn.org/courses")
    data=URL.json()
    with open("new.json","w") as num:
        json.dump(data,num,indent=4)
    q=open("new.json","r")
    read=q.read()
    data=json.loads(read)
serial_no=0
for i in range(0,len(data)):
    print(serial_no+1,".",data[i]["name"],"ID:",data[i]["id"])
    serial_no+=1
courses_name=int(input("enter your course number which you want to learn   :"))
print(data[courses_name-1]["name"])
H=data[courses_name-1]["id"]
a=data[courses_name-1]["name"]+"_"+H+".json"
# print(courses_name)
if os.path.exists(a):
    file=open(a,"r")
    k=file.read()
    data=json.loads(k)
else:
    URL2=requests.get('https://api.merakilearn.org/courses/'+str(data["course"][courses_name-1]["id"])+"/exercises")
    print(URL2)
    file=URL2.json()
    with open("data1.json","w") as file1:
        json.dump(file,file1,indent=4)
    q=open(a,"r")
    read=q.read()
    data=json.loads(read)
list2=[]
data=0                    
data_1=1
for i in file["course"]["exercises"]:   
    if i["parent_exercise_id"]==None:
            data=data+1
            list2.append(i)
    if i["parent_exercise_id"]==i["id"]:
            print(data+1,".",i["name"])
            list2.append(i)
            data=data+1   
    if i["parent_exercise_id"]!=i["id"]:
            print(" ",data_1,".",i["name"])
            list2.append(i)
    data_1=data_1+1
with open("data2.json","w") as f:
    json.dump(list2,f,indent=4)
topic_no=int(input("choose topic number which you want to learn : "))
for l in range(0,len(list2)):
    if topic_no==l+1:
        print(topic_no,list2[l]["name"])
        a=list2[l]["parent_exercise_id"]
var=1
var_1=[]
var_2=[]
for d in range(0,len(list2)):
    if list2[d]["parent_exercise_id"]==a:
        print(" ",var,list2[d]["name"])
        var_1.append(list2[d]["name"])
        var_2.append(list2[d]["content"])
        var+=1
child_number=int(input("which child you want to print : "))
print(topic_no,list2[l]["name"])
print(var_2[child_number-1])
question=child_number-1
while child_number>0:
# Here a taking user input in a previous or next
    next_question=input("do you next question or previous question n/p :- ")
    if child_number==len(var_2):
        print("next page")
    if next_question=="p":
        if child_number==1:
            print("no more questions")
            while i<len(list2):
                print(topic_no,list2[l]["name"])
                print(var_2[child_number-1])
        else:
            child_number=child_number-1
            print(var_2[child_number])
    if next_question=="n":
        if child_number<len(var_2):
            index=child_number+1
            print(var_2[index-1])
            question=question+1
            child_number=child_number+1 
            if question==(len(var_2)-1) :
                print("next page")              
                break
	
