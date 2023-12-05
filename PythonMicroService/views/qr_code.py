from django.http import JsonResponse
from PythonMicroService.service.qr_code import QRCode
import base64
from django.shortcuts import render
from io import BytesIO

def hello(request):
    return JsonResponse({'message': "Ok"})


def generate_qr_code(request, text):
    image = QRCode().generate_qr_code(text=text)  # this is an image object

    # Convert the image to base64
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return render(request, "qr_code.html", {"image": img_str })