import openai
import os
import pyttsx3

# Store chat history for better conversation flow
chat_history = []

engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatbot_response(user_input):
    """Generates a response using OpenAI's GPT-4 model, considering past interactions."""
    openai.api_key = "your_openai_api_key"  # Replace with your API key
    
    # Append user input to chat history
    chat_history.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a supportive and empathetic mental health chatbot."}
        ] + chat_history  # Include chat history in messages
    )
    
    bot_response = response["choices"][0]["message"]["content"]
    chat_history.append({"role": "assistant", "content": bot_response})  # Store bot response
    
    return bot_response

def detect_urgent_message(user_input):
    """Detects if the user expresses distress or suicidal thoughts and provides emergency help links."""
    crisis_keywords = ["suicide", "hurt myself", "end my life", "depressed", "hopeless"]
    
    if any(keyword in user_input.lower() for keyword in crisis_keywords):
        return ("I'm really sorry you're feeling this way. "
                "You are not alone. Please reach out to a professional or contact a crisis helpline: "
                "91-9820466726 or a local support service.")
    return None

def main():
    print("Mental Health Chatbot: Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Take care! Remember, you are not alone.")
            break
        
        # Check for crisis messages
        urgent_response = detect_urgent_message(user_input)
        if urgent_response:
            print(f"Chatbot: {urgent_response}")
            continue
        
        # Generate AI response with memory
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        
if __name__ == "__main__":
    main()
