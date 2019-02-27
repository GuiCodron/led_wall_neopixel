import unicodedata
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

CHARS_MATRIX = {}

def char_to_pixels(text, path='arialbd.ttf', fontsize=12):
    """
    Based on https://stackoverflow.com/a/27753869/190597 (jsheperd)
    """
    font = ImageFont.truetype(path, fontsize)
    w, h = font.getsize(text)
    h *= 2
    image = Image.new('L', (w, h), 1)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), text, font=font)
    arr = np.asarray(image)
    arr = np.where(arr, 0, 1)
    arr = arr[(arr != 0).any(axis=1)]
    return arr

def init_char_matrix(width):
    for c in "qwertyuioplkjhgfdsazxcvbnm ,.'":
        CHARS_MATRIX[c.upper()] = char_to_pixels(c.upper(), './LiberationMono-Bold.ttf', width)

class TextDisplayer():
    default_color = (0, 0, 123)
    def __init__(self, pixels_strips, strip_offset=0):
        self.pixels_strips = pixels_strips
        self.strip_offset = strip_offset
        pass

    def set_letter(self, letter, position):
        if not letter.upper() in CHARS_MATRIX:
            return (0, False)
        displayed = False
        char_mat = CHARS_MATRIX[letter.upper()]
        letter_size = char_mat.shape[1]
        if (position) > len(self.pixels_strips[0]):
            return (-1, False)

        if position + letter_size > 0 and position < len(self.pixels_strips[0]):
            displayed = True

        for i, char_line in enumerate(char_mat):
            if i >= len(self.pixels_strips):
                print("overflow i", i, "len", len(self.pixels_strips))

                break
            for j, v in enumerate(char_line):
                if position + j > 0 and position + j < len(self.pixels_strips[self.strip_offset + i]):
                    # print("pos",position, "idx", position + j)
                    self.pixels_strips[self.strip_offset + i][position + j] = self.default_color if (v == 1) else 0

        return (letter_size, displayed)


    def display_text(self, text1, text2, position=0):
        self.clear()
        text_end = False
        for ti, text in enumerate((text1, text2)):
            c_width = 0
            letters_count = 0
            for i, c in enumerate(text):
                if unicodedata.category(c) == 'Mn':
                    continue
                c = unicodedata.normalize('NFD', c)
                c_width, displayed = self.set_letter(c, position)

                if displayed:
                    letters_count += 1

                if c_width == -1:
                    break
                if c_width > 0:
                    position += c_width + 1
            # Check if whole text was skipped
            if letters_count == 0 and ti == 0:
                text_end = True
            # Check if text1 is enough
            if c_width == -1:
                break
        for strip in self.pixels_strips:
            strip.show()

        return text_end

    def clear(self):
        for pixels in self.pixels_strips:
            pixels.fill(0)
            pixels.show()
