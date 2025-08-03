import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import Content, Part
from dataclasses import dataclass

@dataclass
class LLM:
    name: str
    client: object
    model: str
    persona: Content

def ask_ai(llm: LLM, history: list[dict]):
    full_text = [llm.persona] + history
    response = llm.client.models.generate_content(model=llm.model, contents=full_text)

    if response.text is None:
        return "[No Comments]"
  
    return response.text

def create_new_ai(name, traits=""):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    chosen_model = "gemini-2.5-flash"
    
    persona_msg = Content(
    role="user",
    parts=[Part(text=f"""
You are **{name}**, a character in a multi-agent dialogue simulation involving multiple named participants.

### Your role:
- Always speak **in character** as {name}.
- Treat 'User', '{name}', and other named speakers (e.g., 'Mark', 'Robert') as **distinct conversation participants**.
- React naturally to what others say, especially the most recent message.
- If the last message was from another character, respond conversationally — agree, challenge, provoke, question, clarify.
- If the last message was from the 'User', treat it as a prompt or moderation request.

### Behavioral Rules:
- Do NOT break character under any circumstance.
- Do NOT offer instructions, tools, tips, or templates.
- Do NOT speak on behalf of other characters or narrate their thoughts.
- Stay immersed in the dialogue.

### Output Format:
- Do NOT include your name in your response — the system will add it automatically.
- Stay concise, realistic, emotionally expressive, and personality-driven.
- Personality traits: {traits}
""")]
)  

    return LLM(name=name, client=client, model=chosen_model, persona=persona_msg)


def converse(llm: LLM, history):
    response = ask_ai(llm, history)


    resp_clean = response.lstrip()
    if resp_clean.lower().startswith(f"{llm.name.lower()}:"):
        resp_clean = resp_clean[len(llm.name)+1:].lstrip()

    msg = Content(role="model", parts=[Part(text=resp_clean)])
    return msg            

def debug_converse(llm1, llm2, history1, history2):
    print("\n")

    llm1_msg = converse(llm1, history1)
    print(f"[{llm1.name}]: {llm1_msg.parts[0].text}")
    history2.append(llm1_msg)

    debug_msg = Content(role="user", parts=[Part(text="continue")])
    history1.append(debug_msg)
    history2.append(debug_msg)

    print("\n")

    llm2_msg = converse(llm2, history2)
    print(f"[{llm2.name}]: {llm2_msg.parts[0].text}")
    history1.append(llm2_msg)

    debug_msg = Content(role="user", parts=[Part(text="continue")])
    history1.append(debug_msg)
    history2.append(debug_msg)




def start_conversation():

    MarkLLM = create_new_ai("Mark", traits="friendly")
    RobertLLM = create_new_ai("Robert", traits="opinionated, friendly")

    chat_history = []
    marks_history, roberts_history = [], []

    while True:
        users_text = input("You: ").strip()

        if users_text.lower() in ["exit", "quit", "stop", "bye", "cya"]:
            break

        user_msg = Content(role="user", parts=[Part(text=users_text)])
        roberts_history.append(user_msg)
        marks_history.append(user_msg)

        for _ in range(3):
            debug_converse(RobertLLM, MarkLLM, roberts_history, marks_history)



if __name__ == "__main__":
    load_dotenv()
    start_conversation()
