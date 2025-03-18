from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth = super().authenticate(request)
        if auth is None:
            raise AuthenticationFailed("You are not authenticated, go to http://127.0.0.1:8000/api/planetarium/create_user/ to register, or login in http://127.0.0.1:8000/api/planetarium/login/")
        return auth
