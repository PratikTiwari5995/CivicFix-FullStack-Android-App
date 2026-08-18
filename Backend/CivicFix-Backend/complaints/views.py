from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ComplaintSerializer
from .models import Complaint


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def complaint_list(request):

    if request.method == 'GET':
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)

        return Response({
            "message": "List of complaints",
            "data": serializer.data
        })

    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": "Complaint created successfully",
                "data": serializer.data
            }, status=201)

        return Response({
            "message": "Failed to create complaint",
            "errors": serializer.errors
        }, status=400)


@api_view(['GET', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def complaint_detail(request, pk):

    try:
        complaint = Complaint.objects.get(pk=pk)
    except Complaint.DoesNotExist:
        return Response({
            "message": "Complaint not found"
        }, status=404)

    if request.method == 'GET':
        serializer = ComplaintSerializer(complaint)

        return Response({
            "message": "Complaint details",
            "data": serializer.data
        })

    if request.method == 'PATCH':
        serializer = ComplaintSerializer(
            complaint,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Complaint updated successfully",
                "data": serializer.data
            })

        return Response({
            "message": "Failed to update complaint",
            "errors": serializer.errors
        }, status=400)

    if request.method == 'DELETE':
        complaint.delete()
        return Response(status=204)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_complaints(request):
    complaints = Complaint.objects.filter(user=request.user)
    serializer = ComplaintSerializer(complaints,
                                     many=True)

    return Response({
        "message": "List of user complaints",
        "data": serializer.data
    })
