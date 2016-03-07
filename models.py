class Post(models.Model):
    owner = models.ForeignKey(User)
    usersVoted = models.ManyToManyField(User, blank=True)
    post = models.CharField(max_length=400)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
