import tkinter as tk
from tkinter import scrolledtext, PhotoImage
from datetime import datetime
import time

# Import the AI response generator from ai.py
from ai import ask_groq as get_ai_response

class NokiaPhoneGame:
    def __init__(self, root):
        self.root = root
        self.root.title("The Stolen Nokia Phone")
        self.root.configure(bg="#424242")
        
        # Set initial window size
        self.root.geometry("350x650")
        self.root.resizable(False, False)

        self.conversation_history = [
            "Charles: Hey Miranda! Can you help me with something?",
            "Charles: It's urgent. Please reply!"
        ]

        # Main phone body frame
        self.phone_body = tk.Frame(root, bg="#1E3A5F", bd=10, relief="raised")
        self.phone_body.pack(padx=20, pady=20)
        
        # Nokia branding
        self.brand_frame = tk.Frame(self.phone_body, bg="#1E3A5F")
        self.brand_frame.pack(fill="x", padx=5, pady=(10, 5))
        
        self.brand_label = tk.Label(self.brand_frame, text="NOKIA", font=("Arial", 16, "bold"), 
                                    bg="#1E3A5F", fg="#D3D3D3")
        self.brand_label.pack(side="right", padx=10)

        # Screen frame with that classic Nokia green
        self.screen_frame = tk.Frame(self.phone_body, bg="#333333", bd=8, relief="sunken")
        self.screen_frame.pack(padx=15, pady=10)

        # Nokia-style screen
        self.screen = scrolledtext.ScrolledText(
            self.screen_frame, width=26, height=8,
            font=("Courier New", 10, "bold"),
            wrap="word", bg="#90EE90", fg="#000000", insertbackground="black",
            borderwidth=0, relief="flat"
        )
        self.screen.pack(padx=5, pady=5)
        self.screen.configure(state='disabled')

        self.screen.tag_configure("message", foreground="black", font=("Courier New", 10, "bold"))
        
        # Status bar for Nokia style (battery, signal)
        self.status_frame = tk.Frame(self.screen_frame, bg="#90EE90", height=15)
        self.status_frame.place(relx=0, rely=0, relwidth=1, height=15)
        
        # Battery indicator
        self.battery_label = tk.Label(self.status_frame, text="🔋", font=("Arial", 8), 
                                      bg="#90EE90", fg="#000000")
        self.battery_label.pack(side="right")
        
        # Signal strength
        self.signal_label = tk.Label(self.status_frame, text="📶", font=("Arial", 8), 
                                    bg="#90EE90", fg="#000000")
        self.signal_label.pack(side="right", padx=(0, 5))
        
        # Current time display
        self.time_label = tk.Label(self.status_frame, text=time.strftime("%H:%M"), 
                                  font=("Arial", 8), bg="#90EE90", fg="#000000")
        self.time_label.pack(side="left", padx=(5, 0))
        
        # Function key area
        self.function_frame = tk.Frame(self.phone_body, bg="#1E3A5F")
        self.function_frame.pack(fill="x", padx=5, pady=5)
        
        # Navigation button (the iconic Nokia circle pad)
        self.nav_frame = tk.Frame(self.function_frame, bg="#1E3A5F")
        self.nav_frame.pack(pady=5)
        
        # D-pad style with center button
        self.nav_up = tk.Button(self.nav_frame, text="▲", font=("Arial", 8), bg="#333333", fg="white", 
                               width=3, height=1, relief="raised")
        self.nav_up.grid(row=0, column=1)
        
        self.nav_left = tk.Button(self.nav_frame, text="◄", font=("Arial", 8), bg="#333333", fg="white", 
                                 width=3, height=1, relief="raised")
        self.nav_left.grid(row=1, column=0)
        
        self.nav_center = tk.Button(self.nav_frame, text="OK", font=("Arial", 8, "bold"), bg="#333333", 
                                   fg="white", width=3, height=1, relief="raised",
                                   command=self.send_message)
        self.nav_center.grid(row=1, column=1)
        
        self.nav_right = tk.Button(self.nav_frame, text="►", font=("Arial", 8), bg="#333333", fg="white", 
                                  width=3, height=1, relief="raised")
        self.nav_right.grid(row=1, column=2)
        
        self.nav_down = tk.Button(self.nav_frame, text="▼", font=("Arial", 8), bg="#333333", fg="white", 
                                 width=3, height=1, relief="raised")
        self.nav_down.grid(row=2, column=1)
        
        # Soft keys
        self.left_soft_key = tk.Button(self.function_frame, text="Menu", font=("Arial", 8), 
                                      bg="#333333", fg="white", width=6, height=1, relief="raised")
        self.left_soft_key.place(relx=0.05, rely=0.5, anchor="w")
        
        self.right_soft_key = tk.Button(self.function_frame, text="Contacts", font=("Arial", 8), 
                                       bg="#333333", fg="white", width=8, height=1, relief="raised")
        self.right_soft_key.place(relx=0.95, rely=0.5, anchor="e")
        
        # Text input area
        self.input_frame = tk.Frame(self.phone_body, bg="#1E3A5F")
        self.input_frame.pack(fill="x", padx=5, pady=(5, 10))
        
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(
            self.input_frame, textvariable=self.input_var,
            font=("Courier New", 10),
            justify="left", bg="#D3D3D3", fg="black", insertbackground="black", bd=1, relief="sunken"
        )
        self.input_entry.pack(fill="x", pady=5)
        self.input_entry.bind("<Return>", self.send_message_event)

        # Keypad frame
        self.keypad_frame = tk.Frame(self.phone_body, bg="#1E3A5F")
        self.keypad_frame.pack(pady=5)

        # Nokia style keypad
        self.keypad = [
            ["1", "2 abc", "3 def"],
            ["4 ghi", "5 jkl", "6 mno"],
            ["7 pqrs", "8 tuv", "9 wxyz"],
            ["*", "0 +", "#"]
        ]

        for i, row in enumerate(self.keypad):
            for j, key in enumerate(row):
                main_char = key[0]
                btn = tk.Button(
                    self.keypad_frame, text=key, font=("Arial", 9, "bold"),
                    width=7, height=2, bg="#333333", fg="white", activebackground="#666666",
                    relief="raised", bd=2, command=lambda k=main_char: self.press_key(k)
                )
                btn.grid(row=i, column=j, padx=2, pady=2)
        
        # Call and end buttons
        self.call_frame = tk.Frame(self.phone_body, bg="#1E3A5F")
        self.call_frame.pack(pady=(5, 10))
        
        self.call_btn = tk.Button(
            self.call_frame, text="📞", font=("Arial", 16),
            width=3, bg="green", fg="white", activebackground="#32CD32",
            command=self.send_message
        )
        self.call_btn.pack(side="left", padx=10)
        
        self.end_btn = tk.Button(
            self.call_frame, text="📵", font=("Arial", 16),
            width=3, bg="red", fg="white", activebackground="#FF4500",
            command=self.backspace
        )
        self.end_btn.pack(side="right", padx=10)
        
        # Initialize conversation history
        for msg in self.conversation_history:
            self.add_message(msg)
            
        # Snake game easter egg
        self.snake_mode = False
        
        # Update clock
        self.update_clock()
        
        self.waiting_for_response = False

    def update_clock(self):
        """Update the clock display every minute"""
        current_time = time.strftime("%H:%M")
        self.time_label.configure(text=current_time)
        self.root.after(30000, self.update_clock)  # Update every 30 seconds

    def press_key(self, char):
        if not self.waiting_for_response:
            current = self.input_var.get()
            self.input_var.set(current + char)

    def backspace(self):
        if not self.waiting_for_response:
            current = self.input_var.get()
            self.input_var.set(current[:-1])
            
    def toggle_snake_mode(self):
        # Easter egg functionality
        if self.snake_mode:
            self.screen.configure(bg="#90EE90", fg="#000000")
            self.status_frame.configure(bg="#90EE90")
            self.battery_label.configure(bg="#90EE90")
            self.signal_label.configure(bg="#90EE90")
            self.time_label.configure(bg="#90EE90")
            self.snake_mode = False
        else:
            self.screen.configure(bg="#000000", fg="#90EE90")
            self.status_frame.configure(bg="#000000")
            self.battery_label.configure(bg="#000000")
            self.signal_label.configure(bg="#000000")
            self.time_label.configure(bg="#000000")
            self.snake_mode = True

    def send_message(self):
        if self.waiting_for_response:
            return

        text = self.input_var.get().strip()
        
        # Easter egg check
        if text.lower() == "snake":
            self.toggle_snake_mode()
            self.input_var.set("")
            return
            
        if text:
            user_msg = f"Miranda: {text}"
            self.conversation_history.append(user_msg)
            self.add_message(user_msg)
            self.input_var.set("")
            self.waiting_for_response = True
            self.set_input_state(False)

            # Simulate typing indicator
            self.screen.configure(state='normal')
            self.typing_indicator = self.screen.index(tk.END)
            self.screen.insert(tk.END, "Charles is typing...\n", "typing")
            self.screen.configure(state='disabled')
            self.screen.see(tk.END)

            # Add delay before response appears
            self.root.after(2000, lambda: self.generate_ai_response(text))  # Send user response as argument
    
    def send_message_event(self, event):
        self.send_message()

    def add_message(self, msg):
        time_str = datetime.now().strftime("%H:%M")
        message_with_time = f"[{time_str}] {msg}"
        self.screen.configure(state='normal')
        self.screen.insert(tk.END, message_with_time + "\n", "message")
        self.screen.configure(state='disabled')
        self.screen.see(tk.END)

    def set_input_state(self, enabled: bool):
        state = "normal" if enabled else "disabled"
        self.input_entry.configure(state=state)
        self.nav_center.configure(state=state)
        self.call_btn.configure(state=state)
        self.end_btn.configure(state=state)
        
        # Disable all keypad buttons
        for child in self.keypad_frame.winfo_children():
            if isinstance(child, tk.Button):
                child.configure(state=state)

    def generate_ai_response(self, user_input):  # User input passed as argument
        # Remove typing indicator before showing response
        self.screen.configure(state='normal')
        
        # Find and delete typing indicator if it exists
        try:
            self.screen.delete(self.typing_indicator, tk.END)
        except:
            pass
            
        self.screen.configure(state='disabled')
        
        # Generate and show response using ai.py
        ai_reply = get_ai_response(user_input)  # Call the function from ai.py
        ai_msg = f"Charles: {ai_reply}"
        self.conversation_history.append(ai_msg)
        self.add_message(ai_msg)
        self.waiting_for_response = False
        self.set_input_state(True)

# Initialize the app
root = tk.Tk()
app = NokiaPhoneGame(root)
root.mainloop()
