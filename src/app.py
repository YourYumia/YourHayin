# standard imports
import json  # noqa: I001
import sys

# non-standard imports
import pathlib

# local imports
import Hayin



def get_file_path(target) -> pathlib.Path:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return pathlib.Path(sys._MEIPASS) / target
    return curr_path / target

questions:tuple[Hayin.QuizEntry] = tuple([] for _ in range(30))# tuple is pre-loaded 
curr_path = pathlib.Path(__file__).resolve().parent
with open(get_file_path("qdb.json"), mode='r', encoding='utf-8') as f:
    # example: questions:[{"input str":"questions","polarity index":0|1,"alignment index":0|1|2}]
    questions = (Hayin.QuizEntry(question) for question in tuple(json.load(f)['questions']))



def ask(query) -> int:
    user_inp:int|str = None
    err:Exception = None
    inp_range = (0, 1, 2, 3)
    
    while user_inp not in inp_range:
        user_inp = input(f"{query}\n\n/> ")
        
        if not user_inp.isdigit():
            err = TypeError
        else:
            user_inp = int(user_inp)-1
            if user_inp not in inp_range:
                err = ValueError
        
        if err != None:
            print(
                f"\n\nInvalid input received! {err}\n",
                "Remember...\n",
                "1. Strongly Disagree",
                "2. Disagree",
                "3. Agree",
                "4. Strongly Agree\n\n"
            )
            continue
    
    return user_inp

  

def run_quiz(player:Hayin.Character, questions) -> Hayin.Character:
    for q in questions:
        points = (-1.0, 0.0, 1.0, 3.0)[ask(q.question)]# [0]:-1 -> [3]:3.0
        player.update_attr(q.target[0], q.target[1], points)
    return player



def main(questions) -> None:
    try:
        player:Hayin.Character = Hayin.Character();
        
        print(f"\nWoah, welcome to the quiz, {player.username}!\n")
        
        print('''
            Your options are (for every question): 1, 2, 3, or, 4.
            1. Strongly Disagree
            2. Disagree
            3. Agree
            4. Strongly Agree\n
        ''')
    
        player = run_quiz(player, questions)
    except KeyboardInterrupt:
        pass
    except RuntimeError:
        pass
    finally:
        print(
            f"\nYou have a {player.get_polarity()} polarity",
            f"and are aligned with the {player.get_alignment()} element!"
        )



if __name__ == "__main__":
    main(questions)