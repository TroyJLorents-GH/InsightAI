from openai_client import OpenAIClient
from extractor import extract_keywords
from logger import log_chat, log_flagged  # make sure this is imported

client = OpenAIClient()

def chat_gpt(prompt):
    flagged, categories = client.moderate_content(prompt)
    if flagged:
        log_flagged(prompt, categories)  # log flagged input separately
        print("[Moderation] Message flagged for:", categories)
        return "Sorry, I can't respond to that."

    response = client.chat_completion(prompt)
    keywords = extract_keywords(prompt)
    log_chat(prompt, response, keywords, categories)
    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        reply = chat_gpt(user_input)
        print("Bot:", reply)
