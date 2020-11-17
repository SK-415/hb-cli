from os import path
import dotenv

env = {
    "HOST": "127.0.0.1",
    "PORT": "8080",
    "SECRET": '',
    "ACCESS_TOKEN": '',
    "SUPERUSERS": [],
    "COMMAND_START": [""],
    "HARUKA_DIR": "./data/"
}


def create_env():
    if path.exists('./.env.prod'):
        return
    with open('.env.prod', 'w') as f:
        pass
    
    for key, value in env.items():
        dotenv.set_key('./.env.prod', key, str(value).replace('\'', '\"'), quote_mode='nerver')

if __name__ == "__main__":
    create_env()