import time

print("🤖 Simple Chatbot (type 'exit' to stop)")

# Define some basic questions and answers
responses = {
    "hii": "Hello! How can I help you today? 😊",
    "hello": "Hello! How can I help you today? 😊",
    "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    "what is your name": "I am your friendly chatbot! 🤖",
    "who created you": "I was created by a developer who loves AI! 🚀",
    "what can you do": "I can answer basic questions! Try asking me something.",
    "what is the time": f"The current time is {time.strftime('%I:%M %p')}.",
    "where are you from": "I exist in the digital world, but you can talk to me from anywhere! 🌍",
    "who is the president of the usa": "As of my last update, the president of the USA is Joe Biden.",
    "bye": "Goodbye! Have a wonderful day! 👋",
    "wait": "I will wait.? 😊",
}

while True:
    user_input = input("You: ").lower()  # Convert input to lowercase

    if user_input == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    # Check if the user input is in responses, otherwise return a default response
    response = responses.get(user_input, "I'm not sure how to answer that. Can you try asking something else?")
    
    print(f"Chatbot: {response}")
