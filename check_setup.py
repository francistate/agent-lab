import os
import sys
 
from dotenv import load_dotenv
 
load_dotenv()
 
print("Python version:", sys.version.split()[0])
assert sys.version_info >= (3, 10), "need Python 3.10 or newer"
 
assert os.getenv("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY missing: check .env"
print("API key: found (hidden)")
 
from llm import chat
 
reply = chat(
    [{"role": "user", "content": "Reply with the single word: ready"}],
    max_tokens=20,
)
print("Model replied:", reply)
