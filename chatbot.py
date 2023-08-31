import tkinter as tk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using patterns and responses
chatbot_responses = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"what's your name|who are you", ["I am a chatbot.", "You can call me ChatBot."]),
    (r"how are you|what’s up", ["I'm just a bot, but I'm doing fine! How can I assist you?"]),
    (r"tell me something",["what can I tell you ?"]),
    (r"which languages can you speak",["I can speak only english."]),
    (r"what is python ?|what is python|what is python?|what is python.",["Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation,and it has fewer syntactical constructions than other languages."]),
    (r"quit|exit|Bye", ["Goodbye!", "See you later!,Thankyou for your time!"]),

]


class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")

        self.chat_log = tk.Text(root, state=tk.DISABLED)
        self.scrollbar = tk.Scrollbar(root, command=self.chat_log.yview)
        self.chat_log['yscrollcommand'] = self.scrollbar.set
        self.user_input = tk.Entry(root)
        self.send_button = tk.Button(root, text="Send", command=self.send_message)

        self.chat_log.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.user_input.pack(padx=10, pady=5, fill=tk.BOTH)
        self.send_button.pack(pady=5)

        self.chat = Chat(chatbot_responses, reflections)

    def send_message(self):
        user_message = self.user_input.get()
        self.user_input.delete(0, tk.END)

        self.update_chat_log("You: " +user_message)

        response = self.get_bot_response(user_message)
        self.update_chat_log("Bot: " +response)

    def update_chat_log(self, message):
        self.chat_log.config(state=tk.NORMAL)
        self.chat_log.insert(tk.END, message + "\n")
        self.chat_log.config(state=tk.DISABLED)
        self.chat_log.see(tk.END)

    def get_bot_response(self, message):
        return self.chat.respond(message)


if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = ChatbotGUI(root)
    root.mainloop()
