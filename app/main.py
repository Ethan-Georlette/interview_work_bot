# entering_point
from app.agent import build_question_prompt, ask_ollama
from app.storage import load_memory_context

memory_context = load_memory_context()
prompt = build_question_prompt(memory_context)
answer = ask_ollama(prompt)
print(answer)
