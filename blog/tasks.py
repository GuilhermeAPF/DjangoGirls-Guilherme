import  string
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from blog.models import Post

def create_random_posts(amount):
    for i in range(amount):
        random_string = get_random_string(10, string.ascii_letters)
        title = f' Random_{random_string}'
        text = get_random_string
        author = User.objects.get(pk=1)

        post = Post.objects.create(
            author=author,
            title=title,
            text=text
        )
        post.publish()
    return f'{amount} posts criados'