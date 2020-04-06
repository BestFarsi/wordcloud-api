#!/usr/bin/python
# -*- coding: utf-8 -*-

from marshmallow import Schema, fields

class WordsSchema(Schema):

    words = fields.Nested("WordSchema", many=True)

class WordSchema(Schema):

    word = fields.String(required=True, default="word")
    count = fields.Integer(required=True, default=1)
