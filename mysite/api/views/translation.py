from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import requests
import re


@csrf_exempt  # allows to bypass djangos CSRF validation, which is need for hanlding API's from non browser clients
@api_view(
    ["POST"]
)  # allows to specify which type of request can be accepted, in this case a post request
def translate(request):  # function definition, passed with the request

    body_data = request.data  # body of data from post request
    translate_text = body_data.get(
        "q", ""
    )  # extracts key value "q", if not defaults to empty string

    # If the input is an empty string
    if (
        not translate_text
    ):  # if empty or none, returns original and translation with empty strings
        return Response({"original_text": "", "translated_text": ""})

    # Check if the input contains only valid alphabetic characters, uses a regex to confirm this.
    if not re.match("^[A-Za-z\\s]+$", translate_text):
        # re(regular expression)module imported is to match regex
        return Response(
            {
                "original_text": translate_text,
                "translated_text": "",  ## returns an empty string
            }
        )

    source_lang = body_data.get("source", "en")  # default to English if not provided
    target_lang = body_data.get("target", "pt")

    # LibreTranslate API request
    response = requests.post(
        "http://127.0.0.1:5000/translate",
        json={
            "q": translate_text,
            "source": source_lang,
            "target": target_lang,
        },
        headers={"Content-Type": "application/json"},
    )

    if response.status_code == 200:  # successful status code form LibreTranslate
        translated_data = (
            response.json()
        )  # converts response from json to python format
        translated_text = translated_data.get(
            "translatedText", ""
        )  # extracts translated text from the response
        return Response(
            {
                "original_text": translate_text,
                "translated_text": translated_text,
            }
        )
    else:
        return Response(
            {"error": "500: Translation service failed."}, status=response.status_code
        )
    
