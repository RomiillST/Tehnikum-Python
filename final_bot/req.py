import requests
sms_token = 'Roman:918812496063'
URL = 'https://api.tehnikum.school/sms/sms.php'
requests.post(URL, data={'token' : sms_token,
                        'sms_phone' : '{}',
                        'sms_text' : '{}'})