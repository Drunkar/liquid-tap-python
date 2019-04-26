# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="liquidtap",
    packages=['liquidtap'],
    version="1.0.1",
    description="QuoineFinancial/LiquidTap websocket client for Python",
    author="Jered Masters",
    author_email="jered.masters@quoine.com",
    url="https://github.com/QuoineFinancial/liquid-tap-python",
    install_requires=['websocket-client!=0.49'],
    keywords=["pusher" "websocket" "client" "liquid" "liquidapi" "liquidtap"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)