import datetime

def chat_logger():
    with open("chat_log.txt", "a") as log_file:
        while True:
            message = input("You: ")
            if message.lower() == "exit":
                print("Chat ended. Messages saved to chat_log.txt.")
                break
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"[{timestamp}] You: {message}\n")

chat_logger()
