from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __init__(self, first_name, last_name, username, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        # Should hash password :
        # self.password = generate_password_hash(password)
        self.password = password


    def to_dict(self):
        return {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "username" : self.username,
            "email" : self.email,
            "password" : self.password,
        }