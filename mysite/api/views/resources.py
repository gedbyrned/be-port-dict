from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from ..models import Resources
from rest_framework import status

import logging

logger = logging.getLogger("mysite")


@csrf_exempt 
@api_view(
    ["GET"]
) 
def resources(request):  
    resource_queryset = Resources.objects.all()

    resource_list = [
        {
            "resource_name": resource.resource_name,
            "resource_type": resource.resource_type,
            "resource_author": resource.resource_author,
            "resource_description": resource.resource_description,
            "resource_level": resource.resource_level,
            "resource_language": resource.resource_language,
            "resource_url": resource.resource_url,
            # Return the full URL to the image stored in S3
            "resource_image": resource.resource_image.url if resource.resource_image else None,
        }
        for resource in resource_queryset
    ]

    ## I am just going to create a restriction on resource_name and resource_type here, these fields neeed to be filled, the rest of the information is optional (for the moment), and test for it.

    # Check if the resource_name and resource_type are filled
    for resource in resource_list:
        if not resource["resource_name"] or not resource["resource_type"]: ##checks if they are falsy, previous checky still leaves fields as truthy
            return Response(
                {"error": "resource_name and resource_type are required fields."},
                 status=status.HTTP_400_BAD_REQUEST
            )

    return Response(resource_list)