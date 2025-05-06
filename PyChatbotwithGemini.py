from google import genai

# Initialize the client with the provided API key
client = genai.Client(api_key="AIzaSyDqgYsOAs2o4C7kavr1mMSxIqeZi5IcTPk")

# Initialize conversation history as a list of messages
conversation_history = []

# Welcome message
print("Welcome to the Chatbot! Type 'quit' to exit.")

# Main chatbot loop
while True:
    user_input = input("You: ").strip()
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye!")
        break
    elif user_input == "":
        print("Please enter a question.")
        continue
    else:
        # Add user input to history
        conversation_history.append("User: " + user_input)
        # Create history string for API call
        history_str = "\n".join(conversation_history)
        try:
            # Generate response using the Gemini model
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=history_str
            )
            assistant_response = response.text
            print("Chatbot:", assistant_response)
            # Add assistant response to history
            conversation_history.append("Assistant: " + assistant_response)
        except Exception as e:
            print("Chatbot: Sorry, I encountered an error. Please try again.")