from classcreation import Question

question_prompts=[
    "What is the color of apple\n a) Red \n b) blue \n c) Magenta\n",
    "What is the color of sky\n a) Red \n b) blue \n c) Magenta\n",
    "What is girls favourite shade\n a) Red \n b) blue \n c) Magenta\n",
]

questions=[Question(question_prompts[0],"a"),
           Question(question_prompts[1],"b"),
           Question(question_prompts[2],"c")
           ]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.question_prompt)
        if answer==question.answer:
            score+=1

    print("You Scored: " + str(score) + " out of " +str(len(questions)))

run_test(questions)