from ebook import Ebook

def main():
    ebook = Ebook("Dasz Radę", "ks Jan Kaczkowski", 320)
    ebook.open()
    ebook.status()
    ebook.next()
    ebook.next()
    ebook.next()
    ebook.next()
    ebook.next()
    ebook.status()
    ebook.close()
    ebook.next()    

if __name__ == "__main__":
    main()





