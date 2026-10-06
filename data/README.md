git clone 

run docker compose up -d
docker exec -it interview-ollama ollama pull {model of ur choosing for example qwen3:8b}
docker cp Modelfile interview-ollama:/tmp/Modelfile
docker exec interview-ollama \
    ollama create interview-agent -f /tmp/Modelfile


############ for slack ##################3
go to your workspace 
add developer app 
add bot token scopes (chat:write,commands)
install to workspace
save in .env in root as SLACK_BOT_TOKEN=
enable socket mode and create token
add in scopes connections:write 
save in .env as SLACK_APP_TOKEN=
go to slash commands and create commands work-start, work-stop
