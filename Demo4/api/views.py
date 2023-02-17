from api.serializers import UserSerializer
from api.models import User
from rest_framework.response import Response
from rest_framework import viewsets


class UserCurd(viewsets.ViewSet):
     def user_list(self,request,id=None):
          user_id = id
          if id is not None:
               usr = User.objects.get(id = user_id)
               serializers = UserSerializer(usr)
                    #json_data = JSONRenderer().render(serializers.data)
                    #return HttpResponse(json_data, content_type ='application/json')
               return Response(serializers.data)
          usr = User.objects.all()
          serializers = UserSerializer(usr, many= True)
          return Response(serializers.data)
     
     def user_create(self,request):
               serializers = UserSerializer(data=request.data)
               if serializers.is_valid():
                    serializers.save()
                    return Response("Add Sucessfully !")
               return Response(serializers.errors)  
      
     def user_update(self,request,id = None):
          user_id = id         
          if id is not None:
               usr = User.objects.get(id = user_id)
               serializers = UserSerializer(usr, data=request.data, partial=True)
               if serializers.is_valid():
                    serializers.save()
               return Response("update Sucessfully !")
          return Response(serializers.errors)
     
     def user_delete(self,request,id=None):
          user_id= id     
          if id is not None:
               usr = User.objects.get(id = user_id)
               usr.delete()
               return Response("delete sucessfully !")
          return Response("ID is NOT FOUND !")

