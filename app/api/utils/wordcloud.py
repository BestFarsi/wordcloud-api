from persian_wordcloud.wordcloud import STOPWORDS, PersianWordCloud
from bidi.algorithm import get_display
from api.utils.config import Config
import arabic_reshaper
from PIL import Image
from os import path
import numpy as np

def convert_persian_text(text):
    new_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(new_text)
    return bidi_text

stopwords = set(STOPWORDS)
twitter_mask = np.array(Image.open(Config.WORDCLOUD_MASK_PATH))
wc = PersianWordCloud(font_step=3, font_path=Config.WORDCLOUD_FONT_PATH,
        background_color="white", max_words=200, mask=twitter_mask, stopwords=stopwords)
