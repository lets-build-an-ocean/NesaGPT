from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from aichatbot.models import Profile, Balance

from aichatbot import serializers


class whoami(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        this_user = request.user
        session = Profile.objects.get(user=this_user)
        serilizer = serializers.ProfileSerilizer(session)
        this_balance = Balance.objects.get(user=this_user)
        data = {
            "username": this_user.username,
            "email": this_user.email,
            "image": serilizer.data,
            "balance": this_balance.wallet,
        }
        return Response(data=data)
