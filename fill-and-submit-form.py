import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "https://crmciec.hostingcrm.com.ar/index.php?module=Users&action=Login"
login_page = browser.get(url)
login_html = login_page.soup  # type: ignore

form = login_html.select("form")[0]

usuario = form.select("input[type=text]")
password = form.select("input[type=password]")
print(usuario)
print(password)



#form.select("input")[0]["value"] = "zeus"
#form.select("input")[1]["value"] = "ThunderDude"

#profiles_page = browser.submit(form, login_page.url)
#print(profiles_page.url)

