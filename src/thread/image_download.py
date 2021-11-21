import urllib.request
import gevent
from gevent import monkey


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    content = req.read()
    with open(img_name, "wb") as f:
        f.write(content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "图片名", "图片链接"),
        gevent.spawn(downloader, "", ""),
        gevent.spawn(downloader, "", ""),
    ])

if __name__ == '__main__':
    main()
