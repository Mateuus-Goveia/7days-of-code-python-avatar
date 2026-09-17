import json
from avatar_client import AvatarClient

if __name__ == "__main__":
    client = AvatarClient()
    personagens = client.listar_personagens()

    if personagens:
        print(json.dumps(personagens, indent=4))