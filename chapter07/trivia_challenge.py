# Trivia Challenge 3.0
# Trivia game that reads a plain text file

# v 2.0 - open_file() function updated to reference a new trvia file that
#         includes points for each question
#         next_block() function now includes return value for points
#         main() function uses the points value to update the score
#
# v 3.0 - added high_scores() function to check whether user has one of top 5
#         scores, if so include in the list

import sys

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    points = next_line(the_file)
    if points:
        points=int(points)      
        
    explanation = next_line(the_file) 

    return category, question, answers, correct, points, explanation

def high_scores(score):
    """Checks user's high score against the current top 5. Adding deails if it is high enough"""
    import pickle
    # load high scores file and extract the scores list
    scores_file=open("High_Scores.dat","rb")
    scorelist=pickle.load(scores_file)
    scores_file.close()

    # loop through current scores and see if user score is higher
    # ensure scores are sorted
    scorelist.sort(reverse=False)
    for scores in scorelist:
        if score >= scores[1]:
            highscore=True
            idx = scorelist.index(scores)
            name = input("Congratulations! You got a high score\n"+\
                         "Please enter your name: ").upper()
            scorelist.insert(idx,[name,score])
            break
        else:
            highscore=False

    if highscore:
        # ensure only top 5 are kept and resort to check alphabetical order
        scorelist.sort(reverse=False)
        scorelist = scorelist[:5]
        scores_file=open("High_Scores.dat","wb")
        pickle.dump(scorelist, scores_file)
        scores_file.close()

    else:
        print("Sorry you didn't make the high score list")

    print("\n\nCurrent high scores:")
    for score in scorelist:
        print("\t",score)

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia_points.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, points, explanation = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += points
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, points, explanation = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("Your final score is", score)

    # check high scores
    high_scores(score)
 
main()  
input("\n\nPress the enter key to exit.")
