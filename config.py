"""Configuration for test and setup.py utilities"""
import os
import sys
import json


docs_bucket = 'quantmind-docs'


def read(name):
    with open(name) as fp:
        return fp.read()
