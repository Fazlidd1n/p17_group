import time

from project.chat.auth.main import File


class Message:
    def __init__(self,
                 from_user: str = None,
                 to_user: str = None,
                 message: str = None,
                 datetime: str = None,
                 is_read: bool = False
                 ):
        self.from_user = from_user
        self.to_user = to_user
        self.message = message
        self.datetime = datetime
        self.is_read = is_read
        self.file = File("users.json")

    def add(self):
        data = {
            "message": self.message,
            "datetime": time.strftime("%Y-%m-%d %H:%M"),
            "is_read": self.is_read
        }
        users = self.file.read()
        for i, user in enumerate(users):
            if self.to_user == user.get("username"):
                if users[i]["messages"][self.from_user]:
                    users[i]["messages"][self.from_user].append(data)
        self.file.write(users)
