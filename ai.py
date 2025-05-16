from groq import Groq
from typing import List, Dict, Optional

client = Groq(api_key="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")

def ask_groq(
    prompt: str,
    temperature: float = 0.7,
    model: str = "llama3-8b-8192",
    system_prompt: str = "You are a helpful assistant.",
    memory: Optional[List[Dict[str, str]]] = None
) -> str:
    """
    Sends a chat completion request to the Groq API and returns the assistant's reply.
    
    Args:
        prompt (str): The user's current prompt/question.
        temperature (float): Controls randomness of the response.
        model (str): The model name to use.
        system_prompt (str): The system prompt defining the assistant's behavior.
        memory (List[Dict[str, str]], optional): List of previous chat messages, each a dict with "role" and "content".
    
    Returns:
        str: The assistant's reply text.
    """
    # Prepare messages starting with system prompt
    messages = [{"role": "system", "content": system_prompt}]
    
    # Append prior conversation memory if given
    if memory:
        messages.extend(memory)
    
    # Append the current user prompt
    messages.append({"role": "user", "content": prompt})
    
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    
    # Return the assistant's response text
    return response.choices[0].message.content


# Example usage with memory
if __name__ == "__main__":
    # Previous conversation history, could be empty initially
    chat_memory = [
        {"role": "user", "content": "Hello, who won the World Cup in 2018?"},
        {"role": "assistant", "content": "France won the 2018 FIFA World Cup."}
    ]

    question = "What about the 2022 winner?"
    answer = ask_groq(question, memory=chat_memory)
    print("Assistant:", answer)
