# django-projects

Note that the file structure is not accurate in this project. This project was put up just to show examples of Django, DRF, AngularJS, Karma and Jasmine in use.

A brief overview of the files in this project:

**models.py**

A Post model exists. Each post has an owner, a usersVoted field (which keeps track of the users who voted to like the post), a post (the actual post which the owner typed out) and a createdAt field (which stores the time and day which the post was created at).

**serializers.py**

The serializer for the post. It includes 3 additional fields.
*1)* voted - a boolean which is true of the user already liked the post, and false otherwise.
*2)* postType - the type of post (in this case, the type of post is just 'posts')
*3)* usersVotedCount - the number of users who liked the post.

When a post is created, the user creating the post (the owner) is automatically added to the list of users who like the post.

**urls.py**

This file routes the URL /posts/ to PostViewSet (the view).

**views.py**

The view in this file is PostViewSet. It uses PostSerializer as the serializer (which users Post as the model). The view has a 'like' and 'unlike' detail_route which allows users to like and unlike a post.

**post.html**

This HTML page has a form which allows users to create a post. It loads post.js and the PostPageApp AngularJS app.

**post.js**

This JS file uses base.js. This JS file has PostPageApp which has a controller which handles the submition of the form in post.html. It calls BaseService.add (the factory in base.js).

**base.js**

This JS file has the factory (called BaseService) which handles post requests to the 'posts' URL (which calls PostViewSet which creates a Post object). It handles the success and error during post creation.


**test_post.js**

This JS file tests the code in post.js (it uses the Jasmine testing framework to test the code and Karma as the test runner).

**karma.conf.js**

This JS file has the configuration for karma (the test runner).
