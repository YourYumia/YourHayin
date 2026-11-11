# standard imports
import json  # noqa: I001
import tkinter as tk
import pathlib
import sys

# non-standard imports
import customtkinter as ctk

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
    user_inp:int|str|None = None
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
            err = None
            continue
    
    return user_inp

  

def run_quiz(player:Hayin.Character, questions) -> Hayin.Character:
    for q in questions:
        points = (-1.0, 0.0, 1.0, 3.0)[ask(q.question)]# [0]:-1 -> [3]:3.0
        player.update_attr(q.target[0], q.target[1], points)
    return player



def main(questions:tuple[Hayin.QuizEntry]) -> None:
    # seting up window for GUI applications
    ctk.set_appearance_mode('system')# theme matches system (light/dark)
    ctk.set_default_color_theme('green')# button and widget colouring

    app = ctk.CTk()# instantiating new window

    app.title='YourHayin by your.yumia'
    app.geometry('960x540')

    init_btn = ctk.CTkButton(master=app, text='BEGIN', width=300,height=60)
    init_btn.widgetName = 'init_btn'
    init_btn.configure(command=init_btn.deletecommand(init_btn.widgetName))
    init_btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    print('past-init-block')
    
    if not init_btn.winfo_exists():
        print('btn gone')
        dummy_txt = ctk.CTkTextbox(master=app, corner_radius=13, border_width=1, border_color='grey')
        dummy_txt.insert('0.0', 'hi from main!')
        dummy_txt.configure(state='disabled')

    app.mainloop()# Launch & keep window open
    
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
    
    print(
        f"\nYou have a {player.get_polarity()} polarity",
        f"and are aligned with the {player.get_alignment()} element!"
    )



if __name__ == "__main__":
    main(questions)