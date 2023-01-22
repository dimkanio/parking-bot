#Telegram bot for users in parking chat

To run the project:

1. Prepare the code of project
```bash
git clone ssh://git@git.******.git
cd parking-bot
```
2. Create in this directory config file .env and add real data
(the easiest way copy .env.example and rename to .env)

3. Build and run
```bash
docker-compose up --build 
```
*Maybe you should correct rules (sudo chmod 666 /var/run/docker.sock)

4. To stop use
```bash
docker-compose down
```



