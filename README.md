# django-projects

Note that the file structure is not accurate in this project. This project was put up just to show examples of Django, DRF, AngularJS, Karma and Jasmine in use.

A brief overview of the files in this project:

models.py:
A Post model exists. Each post has an owner, a usersVoted field (which keeps track of the users who voted to like the post), a post (the actual post which the owner typed out) and a createdAt field (which stores the time and day which the post was created at).

serializers.py:
The serializer for the post. It includes 3 additional fields.
1) voted - a boolean which is true of the user already liked the post, and false otherwise.
2) postType - the type of post (in this case, the type of post is just 'posts')
3) usersVotedCount - the number of users who liked the post.

When a post is created, the user creating the post (the owner) is automatically added to the list of users who like the post.

