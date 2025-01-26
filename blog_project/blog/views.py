from django.shortcuts import render

# Create your views here.
BLOG_POSTS = {
    "my-first-post": {
        "title": "My first post",
        "content": "Hello world! This is my first post.",
        "date": "November 20, 2020"
    },
    "my-second-post": {
        "title": "My second post",
        "content": "Hello world! This is my second post.",
        "date": "November 20, 2020"
    }
}

def home(request):
    return render(request, 'blog/home.html', {'posts': BLOG_POSTS})

def post_details(request, slug):
    post = BLOG_POSTS.get(slug)
    return render(request, 'blog/post_detail.html', {'post': post})