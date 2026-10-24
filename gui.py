import tkinter as tk
from tkinter import ttk, messagebox
from main import algorithms, solve, read_state
delay = 500

path = []          
step = 0          
playing = False 


root = tk.Tk()
root.title("8 puzzle solver")


def show(state):
    """show one state on the board"""
    for pos, tile in enumerate(state):
        cells[pos].config(text=str(tile),
                          bg="#dddddd" if tile == 0 else "#7ab8ff")


def update_view():
    """show the current step of the path"""
    if not path:
        return
    show(path[step])
    step_label.config(text=f"Step {step} / {len(path) - 1}")


def on_solve():
    """read the inputs, run the chosen search and show the first state"""
    global path, step, playing
    try:
        state = read_state(entry.get())
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))
        return

    choice = algo.current() + 1            #index zero based: choice 1..5
    step_label.config(text="Searching...")
    root.update()                         

    result = solve(state, choice)
    path, step, playing = result["path"], 0, False
    play_btn.config(text="Play")
    stats.config(text=(
        f"path cost     : {result['pathcost']}\n"
        f"nodes expanded: {result['node_count']}\n"
        f"search depth  : {result['depth']}\n"
        f"running time  : {result['totaltime']: .5f} s"))
    update_view()


def next_step():
    global step
    if path and step < len(path) - 1:
        step += 1
        update_view()


def prev_step():
    global step
    if path and step > 0:
        step -= 1
        update_view()


def auto_step():
    """move one step forward every 0.5 s until the goal or Pause."""
    global playing
    if playing and path and step < len(path) - 1:
        next_step()
        root.after(delay, auto_step)
    else:
        playing = False
        play_btn.config(text="Play")


def toggle_play():
    global playing
    playing = not playing
    play_btn.config(text="Pause" if playing else "Play")
    if playing:
        auto_step()
def toggle_speed():
    global delay
    delay = 125 if delay == 500 else 500
    speed_btn.config(text="4x" if delay == 125 else "1x")


# forinput row
top = tk.Frame(root)
top.pack(padx=10, pady=10)
entry = tk.Entry(top, width=22)
entry.insert(0, "1,2,5,3,4,0,6,7,8")
entry.grid(row=0, column=0, padx=5)
algo = ttk.Combobox(top, values=list(algorithms.values()), state="readonly", width=16)
algo.current(0) # default:bfs
algo.grid(row=0, column=1, padx=5)
tk.Button(top, text="Solve", command=on_solve).grid(row=0, column=2, padx=5)

# board 
board = tk.Frame(root)
board.pack()
cells = []
for pos in range(9):
    lbl = tk.Label(board, width=4, height=2, font=("Arial", 28, "bold"),
                   relief="ridge", bd=3)
    lbl.grid(row=pos // 3, column=pos % 3, padx=2, pady=2)
    cells.append(lbl)

#controls 
step_label = tk.Label(root, text="Press Solve", font=("Arial", 12))
step_label.pack(pady=5)
ctrl = tk.Frame(root)
ctrl.pack()
tk.Button(ctrl, text="< Prev", command=prev_step).grid(row=0, column=0, padx=3)
play_btn = tk.Button(ctrl, text="Play", width=6, command=toggle_play)
play_btn.grid(row=0, column=1, padx=3)
speed_btn = tk.Button(ctrl, text="1x", width=4, command=toggle_speed)
speed_btn.grid(row=0, column=2, padx=3)
tk.Button(ctrl, text="Next >", command=next_step).grid(row=0, column=3, padx=3)

#statistics
stats = tk.Label(root, text="", justify="left", font=("Consolas", 10))
stats.pack(pady=10)


show(read_state(entry.get()))

root.mainloop()