from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "User registered successfully."}
            , status=201)

    
    return Response({
        "message": "Registration failed",
        "errors": serializer.errors
    }, status=400)

