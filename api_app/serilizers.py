from rest_framework.serializers import ModelSerializer
from .models import *

class Machine(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # exclude = 'mobile'
        # fields = ('first_name', 'email', 'last_name')