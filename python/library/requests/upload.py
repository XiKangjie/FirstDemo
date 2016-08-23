import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

m = MultipartEncoder(
    fields={
            'file': ("test.cfg", open('test.cfg', 'rb'), 'text/plain')}
    )
#print m.to_string()
r = requests.post('http://localhost:9000/upload', data=m,
                  headers={'Content-Type': m.content_type})
print r.text
