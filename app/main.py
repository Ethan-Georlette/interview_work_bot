# entering_point
from app.agent import build_question_prompt, ask_ollama, generate_question
from app.session import start_session
from app.storage import load_memory_context, save_curr_session

session = start_session()
save_curr_session(session)
mem = load_memory_context()
question = generate_question(mem,session)
print(question)
