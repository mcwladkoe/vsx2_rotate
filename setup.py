import os
from setuptools import setup

import config

b = os.path.dirname(__file__)

setup(
    name='vsx2_rotate',
    version='1.0.0',
    author='Vladyslav Samotoy',
    author_email="svevladislav@gmail.com",
    maintainer_email="vsx2.com",
    url="https://github.com/mcwladkoe/vsx2_rotate",
    license="GNU GPL-3.0",
    long_description=config.read(os.path.join(b, 'README.md')),
    packages=['vsx2_rotate'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU GPL-3.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
