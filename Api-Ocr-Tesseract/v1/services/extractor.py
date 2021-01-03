import numpy as np
import pytesseract
from fastapi import File
from settings import Settings
from PIL import Image
from io import BytesIO
from v1.modules.utils import cronometra

def bytes_to_ndarray(bytes):
    bytes_io = bytearray(bytes)
    img = Image.open(BytesIO(bytes_io))
    return np.array(img)

class Extractor():
    def __init__(self):
        self.cfg = Settings()

    @cronometra
    def run(self, file: bytes = File(...)):
        try:
            nparr = np.fromstring(file, np.uint8)

            image = Image.open(BytesIO(nparr))
            dict_ext = {}
            text = pytesseract.image_to_string(image, lang='por')
            dict_ext['data'] = text
            dict_ext['version'] = self.cfg.version

            return dict_ext
        except Exception as e:
            print(e)
            return {"status": "failed", "data": None, 'message': "Unknown error",
                    "error": {"code": 3, "raised": e.__class__.__name__, "message": " Error Message:" + str(e)}}, 200