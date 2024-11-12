
from datetime import datetime

class Post:
    def __init__(self, text):
        self.text = text
        self.user = None
        self.created_at = datetime.now()

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.text}"

    def set_user(self, user):
        self.user = user

class TextPost(Post):
    def __init__(self, text):
        super().__init__(text)

class PicturePost(Post):
    def __init__(self, text, image_url):
        super().__init__(text)
        self.image_url = image_url

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.text}\n  Pic URL: {self.image_url}"

class CheckInPost(Post):
    def __init__(self, text, latitude, longitude):
        super().__init__(text)
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.text}\n  {self.latitude}, {self.longitude}"
