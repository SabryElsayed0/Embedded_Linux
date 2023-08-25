import webbrowser
favorite_URLS = [
    "https://www.facebook.com/",
    "https://www.linkedin.com/?original_referer=https%3A%2F%2Fwww.google.com%2F",
    "https://github.com/"
]

def FavoriteWebSites():
    print("Please Choice your desired link")
    print("1 - for facebook website")
    print("2 - for LinkedIn website")
    print("3 - for GitHub website")
    x = int(input("Enter 1 or 2 or 3 \n"))
    webbrowser.open(favorite_URLS[x - 1])
    
FavoriteWebSites()