import tkinter as tk
from tkinter import scrolledtext

class OldPhoneGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Retro Phone Game")
        self.root.configure(bg="dimgray")

        # Phone body
        self.phone_frame = tk.Frame(root, bg="#222", bd=15, relief="ridge")
        self.phone_frame.pack(padx=30, pady=30)

        # Screen (chat)
        self.screen = scrolledtext.ScrolledText(
            self.phone_frame, width=30, height=10, font=("Courier New", 11),
            wrap="word", bg="#003300", fg="#33FF33", insertbackground="white",
            borderwidth=3, relief="sunken"
        )
        self.screen.grid(row=0, column=0, columnspan=3, pady=(0, 10))
        self.screen.configure(state='disabled')

        # Input field
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self.phone_frame, textvariable=self.input_var, font=("Courier New", 11),
            justify="left", bg="#222", fg="white", insertbackground="white", bd=2, relief="groove"
        )
        self.input_entry.grid(row=1, column=0, columnspan=3, sticky="we", padx=5, pady=(0, 10))
        self.input_entry.bind("<Return>", self.send_message_event)

        # Keypad
        self.keypad = [
            ["1", "2 ABC", "3 DEF"],
            ["4 GHI", "5 JKL", "6 MNO"],
            ["7 PQRS", "8 TUV", "9 WXYZ"],
            ["*", "0", "#"]
        ]

        for i, row in enumerate(self.keypad):
            for j, key in enumerate(row):
                btn = tk.Button(
                    self.phone_frame, text=key, font=("Courier New", 10),
                    width=8, height=2, bg="#444", fg="white", activebackground="#666",
                    relief="raised", bd=3, command=lambda k=key: self.press_key(k[0])
                )
                btn.grid(row=i + 2, column=j, padx=3, pady=3)

        # Send and Backspace buttons
        self.send_btn = tk.Button(
            self.phone_frame, text="Send", font=("Courier New", 10),
            width=10, bg="#006400", fg="white", activebackground="#228B22",
            command=self.send_message
        )
        self.send_btn.grid(row=6, column=0, pady=(10, 0))

        self.back_btn = tk.Button(
            self.phone_frame, text="Backspace", font=("Courier New", 10),
            width=20, bg="#8B0000", fg="white", activebackground="#B22222",
            command=self.backspace
        )
        self.back_btn.grid(row=6, column=1, columnspan=2, pady=(10, 0))

        # Initial messages
        self.add_message("Friend: Hey! Can you help me with something?")
        self.add_message("Friend: It’s urgent. Please reply!")

    def press_key(self, char):
        current = self.input_var.get()
        self.input_var.set(current + char)

    def backspace(self):
        current = self.input_var.get()
        self.input_var.set(current[:-1])

    def send_message(self):
        text = self.input_var.get()
        if text.strip():
            self.add_message("You: " + text.strip())
        self.input_var.set("")

    def send_message_event(self, event):
        self.send_message()

    def add_message(self, msg):
        self.screen.configure(state='normal')
        self.screen.insert(tk.END, msg + "\n")
        self.screen.configure(state='disabled')
        self.screen.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = OldPhoneGame(root)
    root.mainloop()
