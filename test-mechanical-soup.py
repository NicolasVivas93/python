import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)
page_html = page.soup  # type: ignore

print(page_html)
print(page_html.prettify())
