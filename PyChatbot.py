import requests

# Input Rapid API key
print("Warning: API key will be visible in output. Clear output after entering.")
RAPID_API_KEY = input("Enter your Rapid API key: ")

# API endpoint for Open AI GPT-3.5 conversation
API_URL = "https://open-ai32.p.rapidapi.com/conversationgpt35"

def get_chatbot_response(user_input):
    """
    Send user input to Rapid API GPT-3.5 endpoint and get response.
    """
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "open-ai32.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "web_access": False
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        
        # Print raw response for debugging
        print("Raw API response:", data)
        
        # Try to extract response (adjust key based on actual response structure)
        if "content" in data:
            return data["content"]
        elif "message" in data:
            return data["message"]
        elif "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0].get("message", {}).get("content", "Error: No message content found.")
        else:
            return "Error: No response found in API data."
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Error connecting to Rapid API: {req_err}"
    except (KeyError, ValueError) as e:
        return f"Error: Invalid response format from Rapid API - {str(e)}"

def main():
    """
    Main function to run the chatbot in Google Colab.
    """
    print("Welcome to the GPT-3.5 Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input.strip():
            print("Please enter a valid question.")
            continue
        
        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    if not RAPID_API_KEY:
        print("Error: No Rapid API key provided.")
    else:
        main()





import requests

# Input Rapid API key
print("Warning: API key will be visible in output. Clear output after entering.")
RAPID_API_KEY = input("Enter your Rapid API key: ")

# API endpoint for Open AI GPT-3.5 conversation
API_URL = "https://open-ai32.p.rapidapi.com/conversationgpt35"

def get_chatbot_response(user_input):
    """
    Send user input to Rapid API GPT-3.5 endpoint and get response.
    """
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "open-ai32.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ],
        "web_access": False
    }
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
        
        # Print raw response for debugging
        print("Raw API response:", data)
        
        # Try to extract response (adjust key based on actual response structure)
        if "content" in data:
            return data["content"]
        elif "message" in data:
            return data["message"]
        elif "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0].get("message", {}).get("content", "Error: No message content found.")
        else:
            return "Error: No response found in API data."
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Error connecting to Rapid API: {req_err}"
    except (KeyError, ValueError) as e:
        return f"Error: Invalid response format from Rapid API - {str(e)}"

def main():
    """
    Main function to run the chatbot in Google Colab.
    """
    print("Welcome to the GPT-3.5 Chatbot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if not user_input.strip():
            print("Please enter a valid question.")
            continue
        
        response = get_chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    if not RAPID_API_KEY:
        print("Error: No Rapid API key provided.")
    else:
        main()