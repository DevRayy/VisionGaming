from cv2 import cv2

import pytesseract
from PIL import Image


def debug_identifier(message):
    def debug_identifier_wrapped(input):
        print(message)
        return message
    return debug_identifier_wrapped


def tesseract(exe_path, data_dir, lang='eng'):
    pytesseract.pytesseract.tesseract_cmd = exe_path

    def tesseract_wrapped(input):
        return pytesseract.image_to_string(Image.fromarray(input), lang=lang, config=data_dir)
    return tesseract_wrapped


def match_template(template_image, method=cv2.TM_CCOEFF):
    def match_template_wrapped(input):
        res = cv2.matchTemplate(input, template_image, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_val, max_loc
    return match_template_wrapped
