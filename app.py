import my_module as mm
import tkinter as tk


def run_app():
    print("Application is executing.")
    root_window = tk.Tk()
    root_window.geometry("300x400")
    open_window = tk.Button(text="Открыть окно", command=mm.module_entry)
    open_window.pack()

    root_window.mainloop()

if __name__ == "__main__":
    run_app()