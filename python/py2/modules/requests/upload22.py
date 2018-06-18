import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder(
    fields={
            'file': ("test.img", open('test.img', 'rb'), 'text/plain')}
    )

r = requests.post('http://localhost:9000/upload', data=m,
                  headers={'Content-Type': m.content_type})
print r.text
