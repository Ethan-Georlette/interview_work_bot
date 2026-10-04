# communitcation with ollama agent
import requests

from app.models import GeneratedQuestion


def build_question_prompt(memory_context: list[str]) -> str:
    return "write an interview question here are the recent topics"\
    + ", ".join(memory_context)


def ask_ollama(prompt: str) -> GeneratedQuestion | None:
    url = 'http://localhost:11434/api/chat'
    data = {
        "model": "interview-agent",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "format": GeneratedQuestion.model_json_schema(),
        "stream": False,
        "keep_alive": 0,
    }
    try:
        answer = requests.post(url, json=data, timeout=(5, 120))
        answer.raise_for_status()
        return GeneratedQuestion.model_validate_json(answer.json()["message"]["content"])
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        print(errh.args[0])
        return None
    except requests.exceptions.Timeout as errrt:
        print(f"Time out: {errrt}")
        return None
    except requests.exceptions.ConnectionError as conerr:
        print(f"Connection error: {conerr}")
        return None
    except requests.exceptions.RequestException as errex:
        print(f"Exception request: {errex}")
        return None
