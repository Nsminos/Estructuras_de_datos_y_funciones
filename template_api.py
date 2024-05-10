from consumir_api import request_json
from string import Template


url_1 = 'https://reqres.in/api/users'
url_2 = 'https://reqres.in/api/users?page=2'
response = request_json(url_1, url_2)
#print(response)
#for elemento in response:
#    print(elemento['images'])
lista_img = [(elemento["images"].get("main"), elemento["name"].get("spanish"), elemento["name"].get("english") ) for elemento in response]
nueva_card = """
        <div class="card" style="width: 18rem;">
            <img src="$url" class="card-img-top" alt="...">
            <div class="card-body">
              <h4 class="text-center">$title_1</h4>
              <h5 class="text-center">$title_2</h5>
            </div>
        </div>"""
#img_template = Template('<img src="$url">')
img_template = Template(nueva_card)
texto_img = ''

#imagen = img_template.substitute(url='https://aves.ninjas.cl/api/site/assets/files/3244/17082018093403canastero_pedro_valencia_web.200x0.jpg')
for img, title_1, title_2 in lista_img:
   texto_img += img_template.substitute(url = img, title_1 = title_1, title_2 = title_2) +'\n'
print(texto_img)
    #print(imagen)  
# – coding: utf-8 –
html_template = Template('''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Aves Ninja</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <h1 class=text-center>Aves de Chile</h1>
    <div class="container">
        <div class="row">
            $body                         
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
''')

html = html_template.substitute(body = texto_img)
archivo = open('index.html', 'w+', encoding="utf-8")
archivo.write(html)
archivo.close()