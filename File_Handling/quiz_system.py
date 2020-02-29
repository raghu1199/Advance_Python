
question_file=open("questions.txt","r")
content=[line.strip() for line in question_file]
question_file.close()
print(content)

score=0
m=0
for i in content:
    q,ans=i.split("=")
    print("Question is:",q)
    user_ans=input("your ans:")
    if ans==user_ans:
        score+=1
    m+=1

res=score/m
res_file=open("results.txt","w")
res_file.write(f"Your final score is {res}.")




