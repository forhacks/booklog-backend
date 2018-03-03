import requests
import urllib2
import re

def generate_website_link(id):
    return "https://www.amazon.com/dp/%s" % id

def get_website(id):
    headers = {"referer": "https://www.amazon.com/dp/%s" % id, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36", "origin" : "https://www.amazon.com", "host" : "www.amazon.com"}

    return requests.get(generate_website_link(id), headers = headers)

def generate_data_link(id):
    return "https://www.amazon.com/gp/search-inside/service-data?method=getBookData&asin=%s" % id

def get_data(id):
    headers = {"Referer": "https://www.amazon.com/dp/%s" % id, "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    return requests.get(generate_data_link(id), headers = headers)


star_regex = re.compile("(\d+\.\d) out of 5 stars")

class AmazonBook:
    def download_website(self):
        self.website = get_website(self.id)

    def download_data(self):
        self.data = get_data(self.id).json()

    def website_downloaded(self):
        return bool(self.website)

    def data_downloaded(self):
        return bool(self.data)

    def __init__(self, id, website = True, data = True):
        self.id = id

        self.website = None
        self.data = None

        if website:
            self.download_website()
        if data:
            self.download_data()

    def get_desc(self):
        if self.website_downloaded():
            text = self.website.text
            findf = "bookDescEncodedData = "

            index = text.find(findf)

            for i in xrange(text.find(findf) + len(findf) + 1, 10000000):
                if (text[i] == '"'):
                    return urllib2.unquote(text[index + len(findf) + 1 : i])

    def get_stars(self):
        if self.data_downloaded():
            json = self.data
            return star_regex.findall(json["reviewStarsImageTag"])[0]


if __name__ == "__main__":
    book = AmazonBook(1847176968)
    print book.get_stars()

