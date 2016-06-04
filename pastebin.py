from urllib.request import urlopen,Request
from urllib.parse import urlencode

def getChangelog():
	req=Request('http://pastebin.com/api/api_login.php')
	req.add_header('api_dev_key','fa1b437a4a1df26eeb9947a0e747f4f1')
	req.add_header('api_user_name','Vambok')
	req.add_header('api_user_password','3BX247')
	api_user_key=str(urlopen(req))
	req=Request('http://pastebin.com/api/api_post.php')
	req.add_header('api_option','paste')
	req.add_header('api_user_key',api_user_key)
	req.add_header('api_paste_name','changelog.txt')
	req.add_header('api_paste_expire_date','1H')
	req.add_header('api_dev_key','fa1b437a4a1df26eeb9947a0e747f4f1')
	req.add_header('api_paste_code',str(open('changelog.txt','r').read()))
	return urlopen(req).read()