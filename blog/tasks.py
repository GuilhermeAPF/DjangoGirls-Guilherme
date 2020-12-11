import string
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from blog.models import Post

from celery import shared_task

@shared_task
def create_random_posts(amount):
    for i in range(amount):
        random_string = get_random_string(10, string.ascii_letters)
        title = f' Random_{random_string}'
        author = User.objects.get(pk=1)

        post = {
            'title': title,
            'text': random_string,
            'author': author.id
        }

        create_random_post.delay(post)


@shared_task
def create_random_post(postdata):
    post = Post.objects.create(author=User.objects.get(pk=postdata['author']), title=postdata['title'], text=postdata['text'])
    post.publish()