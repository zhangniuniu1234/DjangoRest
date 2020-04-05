from rest_framework import  serializers

from Two.models import Person, Blog


# class PersonSerializers(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     p_name=serializers.CharField(max_length=32)
#     p_age=serializers.IntegerField(default=1)
#     def update(self, instance, validated_data):
#        instance.p_name=validated_data.get("p_name",instance.p_name)
#        instance.p_age=validated_data.get("p_age") or instance.p_age
#        instance.save()
#        return instance
#
#     def create(self, validated_data):
#         return Person.objects.create(**validated_data)

#也可以继承serializers.HyperlinkedModelSerializer 超链接，不推荐使用问题多
class  PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=("id","p_name","p_age")


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=("id","b_title","b_content")

