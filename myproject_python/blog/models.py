from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the article.
        content (str): The content of the article.
        author (User): The author of the article.
        created_at (datetime): The date and time the article was created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title