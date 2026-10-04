import json

class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name, age):
        user = {"id": self.next_id, "name": name, "age": age}
        self.users.append(user)
        self.next_id = self.next_id + 1
        return user

    def get_user(self, uid):
        for u in self.users:
            if u["id"] == uid:
                return u
        return None

    def update_age(self, uid, new_age):
        u = self.get_user(uid)
        if u is None:
            return False
        u["age"] = new_age
        return True

    def remove_user(self, uid):
        u = self.get_user(uid)
        if u is None:
            return False
        self.users.remove(u)
        return True

    def list_users(self):
        return self.users

    def save_to_json(self, filepath):
        f = open(filepath, "w", encoding="utf-8")
        json.dump(self.users, f, ensure_ascii=False)
        f.close()

    def load_from_json(self, filepath):
        f = open(filepath, "r", encoding="utf-8")
        data = json.load(f)
        f.close()
        self.users = data
        max_id = 0
        for u in self.users:
            if u["id"] > max_id:
                max_id = u["id"]
        self.next_id = max_id + 1