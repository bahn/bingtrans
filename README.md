Bingtrans
=========

Bingtrans is a Python library for interfacing with Microsoft Translate API.

Bingtrans is licensed under the [Apache Licence, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

Features
--------

Bingtrans can:

- translate a text or html file in a language into another language

You are welcomed to expand this module.

Install
-------

python ./setup.py install

Example
-------

~~~~.python
import bingtrans
bingtrans.set_app_id(YourAppID)  # you can get your AppID at: http://www.bing.com/developers/
print bingtrans.translate('hello', 'en', 'ko')
~~~~

Homepage
--------

http://github.com/bahn/bingtrans

Byung Gyu Ahn <<bahn@cs.jhu.edu>>
