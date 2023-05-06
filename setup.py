from setuptools import setup, find_packages

setup(
    name='screenshots_pagepixels',
    version='1.0.0',
    description='Take immediate screenshots, create scheduled screenshots, take multi-step screenshots (click links, complete forms, login to websites), and get change notifications using the PagePixels Screenshot API python wrapper.',
    author='PagePixels LLC',
    author_email='support@pagepixels.com',
    url='https://github.com/yourusername/screenshots_pagepixels',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
