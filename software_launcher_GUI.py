import tkinter as tk

window = tk.Tk()
window.geometry("1100x600")
window.title("Software Launcher GUI 0.0.1")
#window.resizable(False, False)
window.configure(background="grey")

def main_menu_software_launcher():
    text = "funzione da implementare :( "
    text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 12))
    text_output.grid(row=285, column=285)

def main_menu_changelog():
    text = """VERSION 0.1.0
        What's new??
        -a bug was fixed that did not allow to open the changelog and credits
        -added the calculator to the software launcher
        -added the rock,paper,scissors game in the software launcher
        -added interactive_book_reader.py in the software launcher
        -fixed changelog bug
        - added credits
        -added the changelog
        -added main menu
        (TO RETURN TO THE MAIN MENU RESTART THE PROGRAM :( )"""
    text_output = tk.Label(window, text=text, fg="black",font=("Helvetica", 12))
    text_output.grid(row=290, column=290)

def main_menu_credits():
    text = """Software created by Mario, if you want to leave a review or suggest an improvement you can write him on discord @ info -Chan#8725  
    (TO RETURN TO THE MAIN MENU RSTART THE PROGRAM :( )"""
    text_output = tk.Label(window, text=text, fg="black", font=("Helvetica", 12))
    text_output.grid(row=301, column=301)

main_menu_A_option = tk.Button(text="Software Launcher", command=main_menu_software_launcher)
main_menu_A_option.grid(row=1, column=100)


main_menu_B_option = tk.Button(text="Changelog", command=main_menu_changelog)
main_menu_B_option.grid(row=287,column=287)


main_menu_C_option = tk.Button(text="Credits", command=main_menu_credits)
main_menu_C_option.grid(row=300,column=300)


if __name__ == "__main__":
    window.mainloop()
