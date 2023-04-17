import tkinter as tk

root = tk.Tk()
root.geometry("300x600")
root.title("Str Reverse Check")

def rev_name(name):
    if name == name[::-1]:
        if name != "":
            reverse = name[::-1]
            answer = f"Result: {name} = {reverse} Nice!"
            return answer
        else:
            error = "Result: "
            return error
    elif name != name[::-1]:
        error1 = f"Result: {name} isnt the same in reverse."
        return error1

def update_name():
    entry = main_entry.get()
    result = rev_name(entry)
    result_label.config(text=f"{result}")

main_text = tk.Label(root, text="Check if given word is the same in reverse")
main_text.pack()

main_entry = tk.Entry(root, )
main_entry.pack()

button = tk.Button(root, text="Go", command=update_name)
button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()