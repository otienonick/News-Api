class News_Source:
    
    '''
    News class to define News Articles Objects

    '''

    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
    

class News_Articles:
    
    '''
    News class to define News source Objects

    '''

    def __init__(self,source,author,title,description,url,urlToImage):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
            
class Everything:

    '''
    Everthing class to define Everything Objects

    '''       
    def __init__(self,title,description,url,urlToImage):
        
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
