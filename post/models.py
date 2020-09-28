from django.db import models
from users import models as user_models


# Create your models here.

#게시글 공통
class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, null=True)
    updated_at = models.DateTimeField(auto_now = True)


#공지사항
class Post_notice(Post):
    def __str__(self):
        return self.title

#질문
class Post_Question(Post):
    pass

#답변
class Post_Answer(Post):
    question = models.ForeignKey(Post_Question, on_delete=models.CASCADE)

