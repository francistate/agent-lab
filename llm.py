from anthropic import Anthropic
from dotenv import load_dotenv
 
load_dotenv()                 # reads .env and exposes ANTHROPIC_API_KEY
client = Anthropic()          # picks the key up from the environment
MODEL = "claude-haiku-5-5"    # claude-haiku-5-5 is small, fast, cheap: ideal for learning
 
 
def chat(messages, system="", max_tokens=1024):
    """Send a list of messages to the model and return its text reply."""
    resp = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=messages,
    )
    return resp.content[0].text
