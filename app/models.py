class Catnews:
    """
    catnews class to define catnews objects
    """
    def __init__(self,id,name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url

class Topnews:
    """
    topnews class to define topnews objects
    """
    def __init__(self,name,author,title,description,urlToImage,url):
        self.name=name
        self.author=author
        self.title=title
        self.description=description
        self.urlToImage=urlToImage
        self.url=url

class Update:
    """
    update class to define catnews objects
    """
    def __init__(self, id, author, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url  
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt