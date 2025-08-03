import os
from dotenv import load_dotenv
from google import genai


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Create the Gemini client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Make the API call
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain what LLMs do in a few words",
    )

    # Print the response
    print(response.text)


if __name__ == "__main__":
    main()
