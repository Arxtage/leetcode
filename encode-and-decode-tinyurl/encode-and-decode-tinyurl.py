import time

class Codec:
    # Using defaultfict
    def __init__(self):
        self.database = collections.defaultdict(str)
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = "http://tinyurl.com/" + str(time.time())
        self.database[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.database[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))