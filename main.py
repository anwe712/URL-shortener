import pyshorteners

def shorten_link(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

original_url = input("Enter the URL you want to shorten: ")
shortened_url = shorten_link(original_url)
print("Shortened URL:", shortened_url)
