print("🙏🙏🙏welcome to kon banega caroadpati🙏🙏🙏")
question_list=["how many contenint are there?",
"what is capital of india?",
"ng me kon se course padhaye jate hai?",
"how many states in indai?"
]
option_list=[["four","nine","seven","eight"],
["chandigarh","bopal","chennai","delhi"],
["software engineering","concilling","tourism","agriculture"],
["30","25","27","29"]
]
solution_list=[3,4,1,4]
ans=["3.seven","4.eight","2.bopal","4.delhi","1.software engineering","3.tourism","2.25","3.29"]
i=0
r=1
y=0
count=0
while i<len(question_list):
    i1=question_list[i]
    print(i1)
    j=0
    k=1
    while j<len(option_list[i]):
        print(k,option_list[i][j])
        k+=1
        j+=1
    lifeline1=input("do you want 5050 lifeline?☎️")
    if lifeline1=="yes":
        print("5050")
        if count==0:
            print(ans[y+i])
            print(ans[y+r])   
            n=int(input("enter answer"))
            if n==solution_list[i]:
                print("👏🥳your answer is correct you win👏🥳get 10000🎟️")
            else:
                print("😞oooh,your answer is wrong game over😞")
                break
            count+=1
        else:
            print("you already used lifeline😞☎️")
            m=int(input("enter answer"))
            if m==solution_list[i]:
                print("👏🥳your answer is correct you win👏🥳get 10000🎟️")
            else:
                print("😞oooh, your answer is wrong game over😞")
                break
    elif lifeline1=="no":
        u=int(input("choose correct answer"))
        if u==solution_list[i]:
            print("👏🥳your answer is correct you win👏🥳get 10000🎟️")
        else:
            print("😞oooh,your answer is wrong game over😞")
            break
    else:
        print("😞oooh,game is over😞")
        break
    i+=1
    r+=1
    y+=1

