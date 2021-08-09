from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["POST"])
def process_image_view(request):
    """
    Receives an image and makes prediction (1 vs 0)
    returns:
    """
    return Response(data={"prediction": 1}, status=status.HTTP_200_OK)
