from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://www.baidu.com/"
    res = urlopen(url)
    with open("baidu.html", mode="w") as f:
        f.write(str(res.read().decode("utf-8")))
    print("Over")
