from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import AllowAny
from core.serializers import RegistrationSerializer
from core.throttle import CustomRateThrottle
from django.contrib.auth import get_user_model


User = get_user_model()


class ListUser(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_classes = [CustomRateThrottle]

    def get(self, request):
        users = list(User.objects.values_list("email", flat=True))
        return Response(
            users,
            status=status.HTTP_200_OK
        )


class RegisterUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyUser(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        is_verified = user.is_verified
        if is_verified:
            return Response(
                {"message": "User is already verified"},
                status=status.HTTP_200_OK
            )
        else:
            orginal_otp = user.otp
            otp_from_user = request.data.get('otp', None)
            if orginal_otp and otp_from_user:
                if otp_from_user == orginal_otp:
                    user.is_verified = True
                    user.save()
                    return Response(
                        {"message": "User verified"},
                        status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {"message": "User not verified"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                raise Exception("OTP validationError")
