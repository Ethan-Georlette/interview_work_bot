# communitcation with ollama agent
import requests


def build_question_prompt(memory_context: list[str]) -> str:
    return "write an interview question here are the recent topics"\
    + ", ".join(memory_context)


def ask_ollama(prompt: str) -> str:
    url = 'http://localhost:11434/api/chat'
    data = {
        "model": "qwen3:8b",
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "stream": False,
    }
    try:
        answer = requests.post(url,json=data)
        answer.raise_for_status()
        return answer.json()["message"]["content"]
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        print(errh.args[0])
        return ""
    except requests.exceptions.ReadTimeout as errrt:
        print(f"Time out: {errrt}")
        return ""
    except requests.exceptions.ConnectionError as conerr:
        print(f"Connection error: {conerr}")
        return ""
    except requests.exceptions.RequestException as errex:
        print(f"Exception request: {errex}")
        return ""
