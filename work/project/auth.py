import json

class Auth:
    def __init__(self, json_path: str) -> None:
        self.json_path = json_path
        self.data = self.load_data(self.json_path)

    def load_data(self, path: str) -> dict:
        with open(path, "r") as f:
            return json.load(f)

    def check_user(self, username: str, password: str) -> bool:
        try:
            return self.data[username] == password
        except KeyError:
            return False


if __name__ == "__main__":
    auth = Auth("./login.json")
    if auth.check_user(input("sup lad, whats ur name? "), input("and ur password? ")):
        print("yos")
    else:
        print("f off")