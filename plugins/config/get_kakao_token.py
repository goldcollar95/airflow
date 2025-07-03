import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '7e20479393e2bda61f75e1a934673b58'
redirect_uri = 'https://example.com/oauth'
authorize_code = '6ydOlKMAISS3lzqUG5BUQN6-jbpNPeXyYm1xrZ8QBLXwSKpcg_OWRQAAAAQKFyEtAAABl837KPro6jj-qNQmaA'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)