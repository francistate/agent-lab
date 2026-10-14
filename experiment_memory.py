from llm import chat

# Test memory by asking the model to remember a name and then recall it
# print(chat([{"role": "user", "content": "My name is Tate."}]))
# print(chat([{"role": "user", "content": "What is my name?"}]))

# Test memory by asking the model to remember a name and then recall it, using a history of messages
history = [{"role": "user", "content": "My name is Tate."}]
history.append({"role": "assistant", "content": chat(history)})
history.append({"role": "user", "content": "What is my name?"})
print(chat(history))
