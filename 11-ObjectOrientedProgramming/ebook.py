class Ebook:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_open = False
        self.current_page = 1

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def status(self):
        print(f"Title: {self.title} \nAuthor: {self.author} \nNumber of pages: {self.number_of_pages}\nCurrent page: {self.current_page}")
    
    def next(self):
        if self.is_open == True:
            self.current_page += 1
        else:
            print(f"Book is closed")

    def previous(self):
        if self.is_open == True:
            self.current_page -= 1
        else:
            print(f"Book is closed")        
