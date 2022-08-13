from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from CQapp.serializers import UserDataSerializer
from CQapp.models import CqUser,CqTeam,Specialty
from rest_framework.response import Response
from django.http import HttpResponse
# Create your views here.

class CQuserView(ModelViewSet):
    queryset = CqUser.objects.all()
    serializer_class = UserDataSerializer

    def create(self, request, *args, **kwargs):
        # import ipdb;ipdb.set_trace()
        data = request.data
        new_user = CqUser.objects.create(first_name=data["first_name"], last_name=data["last_name"],
                                         email=data["email"], role=data["role"])
        new_user.save()
        splobj = [Specialty.objects.get(id=spec["id"]) for spec in data["specialties"]]
        for spl in splobj:
            new_user.specialties.add(spl)
        teamobj = [CqTeam.objects.get(id=members["id"]) for members in data["members"]]
        for team1 in teamobj:
            new_user.members.add(team1)
        serializer = UserDataSerializer(new_user)
        return Response(serializer.data)


    def update(self, request, pk):
        obj = CqUser.objects.get(id=pk)
        data = request.data
        if obj:
            obj.first_name = data["first_name"]
            obj.last_name = data["last_name"]
            obj.email = data["email"]
            obj.role = data["role"]
            obj.save()


        splist1 = []
        obj.specialties.clear()
        a = len(data['specialties'])
        for z in range(a):
            sp = Specialty.objects.all().filter(name=data['specialties'][z]['name'])
            for i in sp:
                splist1.append(i)
        print(splist1)
        for i in splist1:
            obj.specialties.add(i)


        splist2 = []
        obj.members.clear()
        c = len(data['members'])
        for z in range(c):
            sp = CqTeam.objects.all().filter(name=data['members'][z]['name'])
            for i in sp:
                splist2.append(i)
        for i in splist2:
            obj.members.add(i)

        serializer = UserDataSerializer(obj)
        return Response(serializer.data)

