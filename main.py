import pyautogui
import time
import pyperclip
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.environ["API_KEY"])

# Use the GenerativeModel
model = genai.GenerativeModel('gemini-1.5-flash')

def is_last_message_from_sender(chat_log, sender_name="Dad"):
    # Print the chat log for debugging
    print("Chat History:", chat_log)
    # Split the chat log into individual messages
    messages = chat_log.strip().split('\n')
    # Check the last message for sender name
    if messages and sender_name in messages[-1]:
        return True
    return False

# Step 1: Click on the Chrome icon at coordinates (1041, 1072)
pyautogui.click(1041, 1072)
time.sleep(1)  # Wait for 1 second to ensure the click is registered

while True:
    time.sleep(5)
    
    # Step 2: Drag the mouse from (-874, 468) to (-545, 1016) to select the text
    pyautogui.moveTo(-874, 468)
    pyautogui.dragTo(-545, 1016, duration=2.0, button='left')  # Drag for 2 seconds

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 2 seconds to ensure the copy command is completed

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()
    
    # Print the copied text to verify
    print("Copied Text:", chat_history)
    
    if is_last_message_from_sender(chat_history):
        try:
            # Generate response from the Gemini model
            prompt = (
                "You are a person named Krish who speaks Roman Nepali as well as English. You are from Nepal and you are a coder. "
                "You analyze chat history reply in funny way . Output should be the next chat response (text message only)."
                "\n\n"
                f"{chat_history}"
            )
            response = model.generate_content(prompt)
            
            # Check for successful response
            if response and response.text:
                generated_text = response.text.strip()
                pyperclip.copy(generated_text)

                # Step 5: Click at coordinates (1808, 1328)
                pyautogui.click(-756,1044)
                time.sleep(1)  # Wait for 1 second to ensure the click is registered

                # Step 6: Paste the text
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

                # Step 7: Press Enter
                pyautogui.press('enter')
            else:
                print("Failed to get a response from the Gemini model.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("The last message is not from the specified sender.")
