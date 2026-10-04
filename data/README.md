git clone 

run docker compose up -d
docker exec -it interview-ollama ollama pull {model of ur choosing for example qwen3:8b}
docker cp Modelfile interview-ollama:/tmp/Modelfile
docker exec interview-ollama \
    ollama create interview-agent -f /tmp/Modelfile