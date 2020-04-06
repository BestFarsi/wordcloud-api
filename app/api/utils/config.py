class Config(object):
    DEBUG = False
    TESTING = False
    WORDCLOUD_MASK_PATH = "resources/twitter_mask.png"
    WORDCLOUD_FONT_PATH = "resources/Vazir-Medium.ttf"
    WORDCLOUD_BASE_STATIC_PATH = "/data"


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
