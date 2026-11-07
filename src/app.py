import Hayin
  

# [0]:Keyo (externalised) / [1]: Dara (internalised) | polarity index

# [0]:desire / [1]:status / [2]:completion | alignment index

questions = (
    Hayin.QuizEntry({
        "input str": "The things I want most are material (i.e. wealth, friends, property, items)",
        "polarity index": 0,# Keyo
        "alignment index": 0# Illio
    }, {
        "input str": "I aspire to be liked and may seek affirmation (i.e. of one's identity, worth, or capability)",
        "polarity index": 0,# Keyo
        "alignment index": 1# Anemo
    }, {
        "input str": "I am most satisfied when I am able to directly support or aid others",
        "polarity index": 0,# Keyo
        "alignment index": 2# Dendro
    }, {
        "input str": "...",
        "polarity index": 1,# Dara
        "alignment index": 0# Paega
    })
)



def ask(query):
    dummy = (1,2,3,4)# will be used to ensure out_i is a valid int (0, 1, 2, 3)
    out_i = 0
    
    try:
        out_i = int(input(f"{query}\n\n/> "))-1
        dummy[out_i]*10# if out_i is not an int or within range of the array an exception will trigger
        return out_i# the index that corresponds to the "points" earned/lost
    except:
        print(
            f"\n\nInvalid input received!\n",
            "Remember...\n",
            "1. Strongly Disagree",
            "2. Disagree",
            "3. Agree",
            "4. Strongly Agree\n\n"
        )
        return ask(query)# exception nests the function once more to create conditional recursion without an explict loop

  

def run_quiz(player:Hayin.Character, questions) -> Hayin.Character:
    for q in questions:
        points = [-1.0, 0.0, 1.0, 3.0][ask(q.question)]# [0]:-1 -> [3]:3.0
        player.update_attr(q.target[0], q.target[1], points)
    return player



def main(questions):
    player = Hayin.Character();

    print(f"\nWoah, welcome to the quiz, {player.username}!\n")

    player = run_quiz(questions)

    print(
        f"\nYou have a {player.get_polarity()} polarity",
        f"and are aligned with the {player.get_alignment()} element!"
    )



if __name__ == "__main__":
    main(questions)