import tkinter as tk

window = tk.Tk()
window.geometry("1100x1000")
window.title("Software Launcher GUI 0.0.1")
#window.resizable(False, False)
window.configure(background="grey")

# row = - riga  column = | colonna

def main_menu_software_launcher():
    interactive_story_reader = tk.Button(text="Interactive Story Reader", command=interactive_story_reader_)
    interactive_story_reader.grid(row=20, column=105)


def main_menu_changelog():
    text = """VERSION 0.0.1
        What's new??
        - added credits
        -added the changelog
        -added main menu
        (TO RETURN TO THE MAIN MENU RESTART THE PROGRAM :( )"""
    text_output = tk.Label(window, text=text, fg="black",font=("Helvetica", 12))
    text_output.grid(row=15, column=450)

def main_menu_credits():
    text = """Software created by Mario, if you want to leave a review or suggest an improvement you can write him on discord @ info -Chan#8725  
    (TO RETURN TO THE MAIN MENU RSTART THE PROGRAM :( )"""
    text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 12))
    text_output.grid(row=15, column=130)


def interactive_story_reader_():
    text = """ message_from_developer: this script is very very bugged, I do not advise you to execute it because it is not yet completed
    ==========================================================================================================================
    
    ===========-NEW STORIES COMING SOON!-======================================================================
    =================-YOU ARE RUNNING THE PRE-ALPHA 0.1.0 VERSION OF INTERACTIVE PYTHON BOOK-==================
    =======================================- TO SEND FEEDBACK WRITE ME ON DISCORD info - Chan #8725 -==========
    
    test"""
    text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 12))
    text_output.grid(row=20, column=110)

main_menu_A_option = tk.Button(text="Software Launcher", command=main_menu_software_launcher)
main_menu_A_option.grid(row=15, column=105)


main_menu_B_option = tk.Button(text="Changelog", command=main_menu_changelog)
main_menu_B_option.grid(row=15,column=115)


main_menu_C_option = tk.Button(text="Credits", command=main_menu_credits)
main_menu_C_option.grid(row=15,column=125)


if __name__ == "__main__":
    window.mainloop()
