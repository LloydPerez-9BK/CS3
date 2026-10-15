class Publication:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")


class Book(Publication):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages if pages > 0 else "Invalid page count"

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue if issue > 0 else "Invalid issue number"

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Issue: {self.issue}")


if __name__ == "__main__":
    book = Book("The Hobbit", "J.R.R. Tolkien", 310)
    magazine = Magazine("National Geographic", "Various Authors", 202)
    pub = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")

    book.display()
    magazine.display()
    pub.display()
