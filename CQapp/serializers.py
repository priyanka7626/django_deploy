from CQapp.models import CqTeam, Specialty, CqUser
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CqTeam
        fields = ('id','name')

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ('id','name')

class UserDataSerializer(serializers.ModelSerializer):
    specialties = SpecialitySerializer(many=True, read_only=True)
    members = TeamSerializer(many=True,read_only=True)

    class Meta:
        model = CqUser
        fields = ('first_name', 'last_name', 'email', 'role', 'specialties','members')
        depth = 1

    # def create(self, validated_data):
    #     specialties = validated_data.pop('specialties')
    #     members = validated_data.pop('members')
    #     user = CqUser.objects.create(**validated_data)
    #
    #
    #     for specialty in specialties:
    #         sp = Specialty.objects.create(**specialty)
    #         user.specialties.add(sp)
    #
    #     for member in members:
    #         CqTeam.objects.create(members=user,**member)
    #
    #     return user

    # def update(self, instance, validated_data):
    #     package = validated_data.pop('package', [])
    #     instance.package.set(self.create_or_update_packages(package))
    #     fields = ['order_id', 'is_cod']
    #     for field in fields:
    #         try:
    #             setattr(instance, field, validated_data[field])
    #         except KeyError:  # validated_data may not contain all fields during HTTP PATCH
    #             pass
    #     instance.save()
    #     return instance

    # def update(self, instance, validated_data):
    #     print()
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.role = validated_data.get('role', instance.role)
    #
    #     x = validated_data['specialties']
    #     print(x)
    #
    #
    #
    #
    #     instance.save()
    #
    #     return instance

