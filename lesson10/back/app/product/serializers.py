from rest_framework import serializers
from .models import Product
from app import settings
from core.serializers import UserSerializer
from comment.serializers import CommentSerializer

class ProductSerializer(serializers.ModelSerializer):
  owner = UserSerializer(read_only=True)
  comment_set = CommentSerializer(many=True, read_only=True)
  image_url = serializers.SerializerMethodField('get_image_url')

  def get_image_url(self, obj):
    return '%s%s' % (settings.MEDIA_URL, obj.image)

  class Meta:
    model = Product
    fields = ('id', 'name', 'price', 'description', 'owner', 'comment_set', 'image', 'image_url')
    read_only_fields = ('owner',)