print("welcome to the chatbot ")
print("write your queries , Type bye anytime to exit")

question_list = {
    "hello":"how can I help ma'am .",
    "tell me about me" : "you are khushi maheshwari, you are recently graduate from b.tech , you are live in bhopal " ,
    "how can i improve my knowlegde":", you must combine structured learning habits with active retrieval strategies. ",
    "tell me some book for reading":" The Science of Successful Learning,methods.Building a Second Brain,The Science of Self-Learning",
    "how to solve difficulty":"To achieve long-term knowledge mastery and efficiently overcome complex challenges, you must transform your approach from passive consumption to structured execution."
}


def solvingFun(userqueries):
    for que in question_list:
        if que in userqueries:
            return question_list[que]
        
       
    # print("Not queires found try something other .....")
            

while True:
    userqueries = input("Enter your question : ")
    result=solvingFun(userqueries)
    print(result)
    if "bye"in userqueries:
        print("thankyou for your time ")
        break





















    # C:\Users\khush\OneDrive\Desktop\python_projects\Rule_based_personal_chatbot.py