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
