import requests

nama = 'Azzam'
print(f'Hello World! to {nama}')
print('Hello World! to {}'.format(nama))

nama_situs = 'ndoware'
try:
    url = f'https://{nama_situs}.com'
    print(url)
    r = requests.get('https://ndoware.com')
    print(r.status_code)
    if r.status_code == 200:
        # print()
        print(r.text)
except Exception as e:
    print('Ada error: ', e)