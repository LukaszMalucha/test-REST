from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    
    serialzier_class = UserSerializer
    
    
class CreateTokenView(ObtainAuthToken):
    
    serialzier_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ManageUserView(generics.RetrieveUpdateAPIView):
    
    serialzier_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        
        return self.request.user