# communitcation with ollama agent



def build_question_prompt(memory_context: list[str]) -> str:
    return "write an interview question here are the recent topics"\
    + ", ".join(memory_context)
