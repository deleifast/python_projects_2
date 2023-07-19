#encoding: iso-8859-1



import functools
import os
import tkinter as tk
from concurrent import futures
 
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)
 
 
def tk_after(target):
 
    @functools.wraps(target)
    def wrapper(self, *args, **kwargs):
        args = (self,) + args
        self.after(0, target, *args, **kwargs)
 
    return wrapper
 
 
def submit_to_pool_executor(executor):
 
    def decorator(target):
 
        @functools.wraps(target)
        def wrapper(*args, **kwargs):
            return executor.submit(target, *args, **kwargs)
 
        return wrapper
 
    return decorator
 
 
class MainFrame(tk.Frame):
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master.geometry('500x350')
        self.master.title("Get output inside GUI")
        self.entry = tk.StringVar()
        label = tk.Label(
            self.master, text="Enter target IP or host as required.")
        label.pack()
        entry = tk.Entry(self.master, textvariable=self.entry)
        entry.insert(-1, "8.8.8.8")
        entry.pack()
        self.button = tk.Button(
            self.master, text="Ping Test", command=self.on_button)
        self.button.pack()
        self.text = tk.Text(self.master)
        self.text.config(state=tk.DISABLED)
        self.text.pack(padx=5, pady=5)
 
    @tk_after
    def button_state(self, enabled=True):
        state = tk.NORMAL
        if not enabled:
            state = tk.DISABLED
        self.button.config(state=state)
 
    @tk_after
    def clear_text(self):
        self.text.config(state=tk.NORMAL)
        self.text.delete(1.0, tk.END)
        self.text.config(state=tk.DISABLED)
 
    @tk_after
    def insert_text(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, text)
        self.text.config(state=tk.DISABLED)
 
    def on_button(self):
        self.ping()
 
    @submit_to_pool_executor(thread_pool_executor)
    def ping(self):
        self.button_state(False)
        self.clear_text()
        self.insert_text('Starting ping request')
 
        result = os.popen("ping "+self.entry.get()+" -n 2")
        for line in result:
            self.insert_text(line)
 
        self.insert_text('ping request finished')
        self.button_state(True)
 
 
if __name__ == '__main__':
    app = tk.Tk()
    main_frame = MainFrame()
    app.mainloop()
