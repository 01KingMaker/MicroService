import pyqrcode
import png
from PIL import Image
from pyzbar.pyzbar import decode
from pyqrcode import QRCode

class QRCode():
    def generate_qr_code(self, text):
        file_path = text + ".png"
        qr_code = pyqrcode.create(text)
        qr_code.png(file_path, scale=6)
        return Image.open(file_path)

    def decode_qr_code(self, qr_code_path):
        image = Image.open(qr_code_path)
        decoded_data = decode(image)    
        for decoded in decoded_data:
            return decoded.data.decode('utf-8')