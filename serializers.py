class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    voted = serializers.SerializerMethodField()
    postType = serializers.SerializerMethodField()
    usersVotedCount = serializers.SerializerMethodField()

    def get_postType(self, obj):
        return 'posts'

    def get_voted(self, obj):
        return self.context['request'].user in obj.usersVoted.all()

    def get_usersVotedCount(self, obj):
        return obj.usersVoted.count()

    class Meta:
        model = Post
        fields = ('id', 'owner', 'usersVotedCount', 'post', 'createdAt', 'voted', 'postType')
        read_only_fields = ('id', 'owner', 'usersVotedCount', 'createdAt', 'voted', 'postType')

    def create(self, validated_data):
        post = Post(
                owner =  validated_data['owner'],
                post = validated_data['post'],
        )
        
        post.save() 

        post.usersVoted.add(validated_data['owner'])

        return post

    # Users should not be allowed to update posts (they should only
    # be able to delete them). No update function needed.
