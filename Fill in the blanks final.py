# -*- coding: utf-8 -*-

#Easy level q/a based on old woman story
easy = {
    'quiz': """There Was an Old Woman Who Lived in a Shoe.\n Once upon a time, there was an old __1__ who lived in a shoe. She had many children. The children were very __2__. They played with almost anything in the shoe. The old woman did not know what to do with her children.\n Suddenly, she had an idea. I shall make them full and then put them all to __3__, thought the old woman. The old woman quickly fed her children with broth until all of them were full.\n Then she tucked them in their beds and put them to sleep.\n Moral of the story :\n Play moderately and always __4__ your parents.""",
    'questions': ["__1__", "__2__", "__3__", "__4__"],
    'answers': ["woman", "playful", "sleep", "obey"]
}


#Medium level q/a based on simple python programming
medium = {
    'quiz': ("A __1__ is created with the def keyword. You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses. __1__s by default return __3__ if you don't specify the value to return. __2__ can be standard data types such as string, number, dictionary, tuple, and __4__ or can be more complicated such as __5__ and lambda functions."),
    'questions': ["__1__", "__2__", "__3__", "__4__", "__5__"],
    'answers': ["function", "variables", "none", "list","objects"]
}

#Hard level q/a based on general knowledge of cricket
hard = {
    'quiz': """ __1__ is a bat-and-ball game played between two teams of __2__ players each on a cricket field, at the centre of which is a __3__ 22-yard-long (20 metres) pitch with a target at each end called the __4__ (a set of three wooden stumps upon which two bails sit). Each phase of play is called an __5__, during which one team bats, attempting to score as many __6__ as possible, whilst their opponents bowl and __7__, attempting to minimise the number of runs scored. When each innings ends, the teams usually __8__ roles for the next innings (i.e. the team that previously batted will bowl/field, and vice versa). The teams each bat for one or two innings, depending on the type of match.""",
    'questions': ["__1__", "__2__", "__3__", "__4__", "__5__", "__6__", "__7__", "__8__"],
    'answers': ["cricket","eleven","rectangular","wicket","innings","runs","fields","sw ap"]
}

#Showing up the quiz to the user based on difficulty level choosen
def play(quiz, max_attempts=4):
    i, attempts = 0, 0
    questions, answers = quiz['questions'], quiz['answers']

    print "\n Let's begin! \n\n", quiz['quiz']

    main_code(i, questions, answers, quiz, max_attempts, attempts)

    print "\n" + "Nice! You have Completed the quiz :)!"

    return play_again()

#function with the main part of our code
def main_code(i, questions, answers, quiz, max_attempts, attempts):
    while i < len(questions):
        if questions[i] in quiz['quiz']:
            question = "What the correct word in replacement for %s? You have %i attempts: " % (questions[i], max_attempts - attempts)
            answer = raw_input(question).lower()

            if answer == answers[i].lower():
                print "That is correct! The answer was %s. The updated quiz is:" % answers[i]
                quiz['quiz'] = quiz['quiz'].replace(questions[i], answers[i])
                i += 1
                attempts = 0
                print "\n", quiz['quiz']
            else:
                attempts += 1
                match_attempts(attempts, max_attempts, answer)
    return 0

#this function compares max attempts to attempts taken
def match_attempts(attempts, max_attempts, answer):
    if attempts >= max_attempts:
        print "\nSorry! No attemps left"
        return play_again()
    else:
        print "\n Sorry, but %s in the wrong answer!" % (answer)
    return 0    

#in case the user completed the quiz and want to try it again with another lever
def play_again():
    user_input = raw_input("\n" + "Would you like to play again ((y)es):").upper()

    if user_input == "YES" or user_input == "Y" or user_input == "y" or user_input == "yes":
        return bootstrap()
    else:
        return '\n' + "Thanks for playing. Bye!" + '\n'

#bootstrap function to determine the difficulty level of the quiz
def bootstrap():
    try:
        while True:
            user_input = raw_input("Easy, Medium or Hard: ").upper()
            if (user_input == "e" or user_input == "E"):
                return play(easy)
            elif (user_input == "m" or user_input == "M"):
                return play(medium)
            elif (user_input == "h" or user_input == "H"):
                return play(hard)

            print '\n' + "Wrong Option! Please choose correct Option:\n"
    except KeyboardInterrupt:
        print "\nBye!"
        pass


print("WELCOME TO THE WORLD OF QUIZ\n"
      "Pick the level you want to play:\n")
bootstrap()
