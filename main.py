import tkinter as tk
from interface import VoiceAssistantInterface
from commands import process_command_func

if __name__ == "__main__":
    root = tk.Tk()
    interface = VoiceAssistantInterface(root, process_command_func)
    root.mainloop()
