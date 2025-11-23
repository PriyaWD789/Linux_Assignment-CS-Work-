import json
import random
import re
import time
from pathlib import Path

# --- 1. Load Knowledge Base ---
def load_knowledge_base(file_path):               
    """Loads the rules from the JSON file."""

    # 1. Get the absolute path of the directory where THIS script is saved
    script_dir = Path(__file__).resolve().parent
    
    # 2. Construct the full path to rules.json
    # It assumes rules.json is right next to the Python script
    file_path = script_dir /"VS CODE STARTED"/"rules.json"
    try:
       with open("file_path", 'r', encoding='utf-8') as f:
             data = json.load(f)
             return data['rules']
    except FileNotFoundError:
        print(f"Error: Knowledge base file not found at {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
        return []

# --- 2. Core Matching Logic ---
def get_response(user_input, rules, current_context):
    """
    Finds a matching rule based on keywords and context.
    
    Args:
        user_input (str): The text entered by the user.
        rules (list): The loaded knowledge base.
        current_context (str): The active context from the last turn.
        
    Returns:
        tuple: (response_text, new_context)
    """
    user_input = user_input.lower()
    
    # 1. Search for matching patterns
    for rule in rules:
        # Check Context Filter first (if a filter exists, the context must match)
        if rule.get("context_filter") and rule["context_filter"] != current_context:
            continue
            
        # Check Keywords/Patterns
        for pattern in rule['patterns']:
            # A simple check: if any word from the pattern is in the user input
            # For better results, use a stricter check (e.g., regex, multiple word match)
            
            # Simple keyword matching: checks if the entire pattern phrase is in the input
            if pattern.lower() in user_input:
                
                # If the current context is set, clear it unless the new intent also sets it.
                new_context = rule.get("context_set", "")
                
                # Return a random response from the matched rule
                return random.choice(rule['responses']), new_context
    
    # 2. Fallback (If no match found)
    # Clear the context on fallback to prevent unwanted follow-ups
    new_context = "" 
    return "I'm sorry, I don't quite understand that. Could you please rephrase or ask about hours, shipping, or payment?", new_context


# --- 3. Main Chat Loop ---
def run_chatbot():
    """Initializes and runs the main chatbot conversation loop."""
# Initialize variables
    rules = load_knowledge_base("file_path")
    if not rules:
        return # Exit if the knowledge base failed to load
        
    current_context = ""
    
    print("-" * 50)
    print("🚀 Rule-Based Support Chatbot Initialized.")
    print("Type 'quit' or 'bye' to exit.")
    print("-" * 50)

    # Start the loop
    while True:
        user_input = input("You: ")
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'bye']:
            # Respond with a goodbye from the JSON if possible, otherwise use a default
            response, _ = get_response("bye", rules, current_context)
            print(f"\nBot: {response}")
            break
            
        # Process the input and get the response
        response, new_context = get_response(user_input, rules, current_context)
        
        # Update context for the next turn
        current_context = new_context
        
        # Display the response
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    run_chatbot()