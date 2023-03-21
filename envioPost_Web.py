import requests
url = 'https://www.celerity.ec/pago-en-linea/'
payload = {'cedula': '1716264344'}
headers = {
    'Host': 'www.celerity.ec',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'https://www.celerity.ec',
    'Content-Type': 'text/html; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.celerity.ec/pago-en-linea/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Cookie': '_gcl_au=1.1.378853639.1679363289; _ga=GA1.1.685055213.1679363289; _gid=GA1.2.492521813.1679363289; _ga_JHDZKLHMFZ=GS1.1.1679363288.1.0.1679363288.0.0.0; _fbp=fb.1.1679363289509.437606668'
    }


response = requests.request("POST", url, headers=headers, data=payload,verify=False)
respuesta = response.text
if respuesta.find('pendiente') > 0:
    print ('se envió post')
else:
    print ('no se envío')

#response = requests.post(url, data=payload)

#print(response.content)