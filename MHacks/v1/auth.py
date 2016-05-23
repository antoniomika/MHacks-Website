from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class Authentication(views.ObtainAuthToken):
    """
    An easy convenient way to log a user in to get his/her token and the groups they are in.
    It also returns other basic information about the user like their name, etc.
    """
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        groups = user.groups.values_list('name', flat=True)
        serialized_user = {'name': user.get_full_name(), 'email': user.email}
        # TODO: Accept push notification token and save it
        return Response({'token': token.key, 'groups': groups, 'user': serialized_user})
