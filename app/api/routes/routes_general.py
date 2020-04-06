#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.wordcloud import wc, convert_persian_text
from api.models.input_schema import WordsSchema
from api.utils.responses import response_with
from flask import Blueprint, current_app, send_from_directory
from api.utils import responses as resp
from flask import request
import multidict
import uuid

route_path_general = Blueprint("route_path_general", __name__)


@route_path_general.route('/wordcloud', methods=['POST'])
def api_wordcloud():
    """
    Create WordCloud endpoint
    ---
    parameters:
        - in: body
          name: body
          schema:
            id: Words
            required:
                - words
            properties:
                words:
                    type: string
                    description: words list to create WordCloud
                    type: array
                    items:
                        schema:
                            id: Word
                            properties:
                                word:
                                    type: string
                                    default: "word"
                                count:
                                    type: integer
                                    default: 1
    responses:
            200:
                description: WordCloud generated successfully
                schema:
                  id: WordCloudCreated
                  properties:
                    filename:
                      type: string
            422:
                description: Invalid input arguments
                schema:
                    id: invalidInput
                    properties:
                        code:
                            type: string
                        message:
                            type: string
    """
    try:
        data = request.get_json()
        words_schema = WordsSchema()
        words, error = words_schema.load(data)
        if error != {}:
            raise Exception("Invalid inputs!")
        filename = "{}.png".format(uuid.uuid4())
        output_name = "{}/{}".format(current_app.config['WORDCLOUD_BASE_STATIC_PATH'], filename)

        word_freqs = multidict.MultiDict()
        for word_item in words['words']:
            word_freqs.add(convert_persian_text(word_item['word']), word_item['count'])

        wc.generate_from_frequencies(word_freqs)
        wc.to_file(output_name)

        return response_with(resp.SUCCESS_200, value={"filename": filename})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)


@route_path_general.route('/file/<path:path>', methods=['GET'])
def api_file(path):
    return send_from_directory('/data', path)
