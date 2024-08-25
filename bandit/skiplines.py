import urllib

path = "https://www.google.com"

if path.startswith(("https:", "http:")):
    with urllib.request.urlopen(path) as resp:  # nosec
        pass
