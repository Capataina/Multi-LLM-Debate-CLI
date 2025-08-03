import os
from dotenv import load_dotenv
from google import genai


def ask_ai(client, model, texts):
    response = client.models.generate_content(model=model, contents=texts)

    print("\n")
    print(response.text)
    print("\n")

    return response.text


def start_conversation():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chosen_model = "gemini-2.5-flash"
    allTexts = []

    while True:
        users_text = input("You: ").strip()

        if users_text.lower() in ["exit", "quit", "stop", "bye", "cya"]:
            break

        users_text = "User: " + users_text

        allTexts.append(users_text)

        response = ask_ai(client, chosen_model, allTexts)

        ai_text = "Gemini: " + (response or "[No response]")

        allTexts.append(ai_text)


def main():
    # Create the Gemini client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Make the API call
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain what LLMs do in a few words",
    )

    # Print the response
    print(response.text)


def test_multi_line():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chat = client.chats.create(model="gemini-2.5-flash")

    response = chat.send_message("I have 2 dogs in my house.")
    print(response.text)

    response = chat.send_message("How many paws are in my house?")
    print(response.text)

    for message in chat.get_history():
        print(f"role - {message.role}", end=": ")
        if message.parts is not None and len(message.parts) > 0:
            print(message.parts[0].text)
        else:
            print("[No content]")


if __name__ == "__main__":
    load_dotenv()
    start_conversation()
