import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser() # creamos el browser para navegar
url = "https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login"

browser.open(url) # abrimos browser y entramos a la url de la webpage
#print(browser.url) # mostramos la url de la web en la que estamos

#print(browser.page) #imprime html de la page
browser.select_form('form[action="index.php"]') #seleccionamos el form pasando: ('tag[atributo=valor]')
#browser.form.print_summary() #imprimimos un resumen de todos los campos en el form

browser["user_name"] = "nicolas.vivas" #seleccionamos el input por el atributo name y le pasamos el value
browser["username_password"] = "12345"
#browser.launch_browser() # lanza una version temporal de un browser real para chequear que todos los datos esten correctamente cargados
#browser.form.print_summary()

response = browser.submit_selected() # hacemos el submit de la información cargada en el form
#print(response.text)

print(browser.page.select("a"))  # type: ignore
