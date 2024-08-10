import random    # imported random module

# quiz set
knowledge_dict = {
    "What is the name of the largest ocean in the world?": "Pacific Ocean",
    "What is the name of the tallest mountain peak in the world?": "Mount Everest",
    "What is the name of the largest ocean in the solar system?": "The Solar System",
    "What is the name of the smallest planet in the solar system?": "Mercury",
    "What is the name of the hottest planet in the solar system?": "Venus",
    "What is the name of the coldest planet in the solar system?": "Neptune",
    "What is the name of the brightest planet in the solar system?": "Venus",
    "What is the name of the planet with the longest day?": "Jupiter",
    "What is the name of the longest river in the world?": "Nile",
    "What is the name of the largest desert in the world?": "Sahara",
    "What is the name of the largest rainforest in the world?": "Amazon",
    "What is the name of the largest country in the world by area?": "Russia",
    "What is the name of the smallest country in the world by area?": "Vatican City",
    "What is the name of the most populous country in the world?": "China",
    "What is the name of the least populous country in the world?": "Vatican City",
    "What is the name of the richest country in the world according to latest Forbes Report?": "United States",
    "Which country has the best education system ?": "United States",
    "What is the name of the poorest country in the world?": "Burundi",
    "What is the name of the oldest country in the world?": "Iran",
    "What is the name of the youngest country in the world?": "South Sudan",
    "What is the name of the most visited country in the world?": "France",
    "What is the name of the least visited country in the world?": "Tulavu",
    "What is the name of the most spoken language in the world?": "Mandarin Chinese",
    "What is the name of the least spoken language in the world?": "Zàpara",
    "What is the name of the most popular sport in the world?": "Soccer",
    "What is the name of the least popular sport in the world?": "Baseball",
    "What is the name of the most famous painting in the world?": "Mona Lisa",
    "What is the name of the most famous sculpture in the world?": "David",
    "What is the name of the most famous book in the world?": "The Lord of the Rings",
    "What is the Capital of India": "New Delhi",
    "Who is the Prime Minister of India": "Narendra Modi",
    "Who is the Creator of Bitcoin": "Satoshi Nakamoto",
    "What is the Currency of India": "Rupee",
    "Who is the President of India": "Droupadi Murmu",
    "Where is the India's Silicon Valley": "Bangalore",
    "What is the India's space agency acronym": "ISRO",
    "What is the Premier tech institute in India": "IIT",
    "What is the National bird of India": "Peacock",
    "What is the National flower of India": "Lotus",
    "What is the National sport of India": "Hockey",
    "What is the National anthem of India": "Jana Gana Mana",
    "What is the National flag of India": "Tricolor",
    "Which is the Highest mountain peak in Indian Subcontinent": "Kanchenjunga",
    "Which is the Longest river in India": "Ganga",
    "Which is the Largest lake in India": "Wular Lake",
    "Which is the Most populous state in India": "Uttar Pradesh",
    "Which is the Least populous state in India": "Sikkim",
    "Which is the Richest state in India": "Maharashtra",
    "Which is the Poorest state in India": "Bihar",
    "Which is the Most literate state in India": "Kerala",
    "Which is the Least literate state in India": "Bihar",
    "Which is the Most developed state in India": "Kerala",
    "Which is the Least developed state in India": "Uttar Pradesh",
    "What is the Full form of CAT exam": "Common Admission Test",
    "What is the Full form of ISRO": "Indian Space Research Organization",
    "Which is the Country with the best education system": "Sweden"
}

keys = list(knowledge_dict.keys())    # list of all questions
question_set = list(knowledge_dict.items()) 

count = 0
wrong_attempts = {}

def evaluate(quest,sol):
    global count
    check = question_set[quest]
    global wrong_attempts
    check = question_set[quest]
    hit = check[1]
    if sol.upper() == hit.upper():
        count+=1
        return True
    wrong_attempts.update({check[0] : check[1]})
    return False

   

def quit():
    print("Thank you for visiting!")


list_of_already_taken_questions = []
def question():
    quest = random.randrange(0, len(question_set))
        
    while (quest in list_of_already_taken_questions):
        quest = random.randrange(0, len(question_set))
    list_of_already_taken_questions.append(quest)
    questions = question_set[quest]
    print(questions[0])
    sol = input("Your answer : ")
    evaluate(quest,sol)

print("Welcome to the General Knowledge Quiz!")

playing = input("Do you want to continue playing?(Please write yes or no) : ")
playing.upper()
if playing == "NO" or playing == "no" or playing == "nO" or playing == "No":
    quit()
else :
    no_of_questions =int(input("How many questions do you want to play against? : "))
    for i in range(no_of_questions):
        question()
    score = count
    
    if score == no_of_questions:
        print("WOW! you got a perfect score")
        print("Your score is ", score," of ", no_of_questions)
        print("You scored ", ((score*100)/no_of_questions),"% in the quiz")
    elif score <= no_of_questions and score >= (no_of_questions//2):
        print("GREAT PLAY! you got a good score. Try harder next time")
        print("Your score is ", score," of ", no_of_questions)
        print("You scored " ,((score*100)/no_of_questions),"% in the quiz")
    elif score > 0 and score < (no_of_questions//2):
        print("A FINE PLAY! you got an average score. Try harder next time")
        print("Your score is ", score," of ", no_of_questions)
        print("You scored ", ((score*100)/no_of_questions),"% in the quiz")
    else :
        print("VERY POOR PLAY! you got to improve a lot. Try harder next time")
        print("Your score is ", score," of ", no_of_questions)
        print("You scored ", ((score*100)/no_of_questions),"% in the quiz")
    print("\n \n \n")
    
    if wrong_attempts != {}:
        print("So here are the answers to the questions you just played against : MAKE SURE TO CHECK THEM OUT :) ")
        wrong_questions = list(wrong_attempts.keys())
        wrong_answers = list(wrong_attempts.values())
        for i in range(len(wrong_attempts)):
            print(wrong_questions[i] + " : " + wrong_answers[i])
        
