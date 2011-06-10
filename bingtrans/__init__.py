"""
Interface to Microsoft Translator API
"""
import urllib
import codecs
import json

api_url = "http://api.microsofttranslator.com/V2/Ajax.svc/Translate"
app_id = ''

def _unicode_urlencode(params):
    """
    A unicode aware version of urllib.urlencode.
    Borrowed from pyfacebook :: http://github.com/sciyoshi/pyfacebook/
    """
    if isinstance(params, dict):
        params = params.items()
    return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params])

def _run_query(args):
	"""
	takes arguments and optional language argument and runs query on server
	"""
	data = _unicode_urlencode(args)
	sock = urllib.urlopen(api_url + '?' + data)
	result = sock.read()
	if result.startswith(codecs.BOM_UTF8):
		result = result.lstrip(codecs.BOM_UTF8).decode('utf-8')
	elif result.startswith(codecs.BOM_UTF16_LE):
		result = result.lstrip(codecs.BOM_UTF16_LE).decode('utf-16-le')
	elif result.startswith(codecs.BOM_UTF16_BE):
		result = result.lstrip(codecs.BOM_UTF16_BE).decode('utf-16-be')
	return json.loads(result)

def set_app_id(new_app_id):
	global app_id
	app_id = new_app_id

def translate(text, source, target, html=False):
	"""
	action=opensearch
	"""
	if not app_id:
		raise ValueError("AppId needs to be set by set_app_id")
	query_args = {
		'appId': app_id,
		'text': text,
		'from': source,
		'to': target,
		'contentType': 'text/plain' if not html else 'text/html',
		'category': 'general'
	}
	return _run_query(query_args)
