books = ["Python", "Java"]

books.append("C++")

book = input("Search book: ")

if book in books:
    print("Found")

books.remove("Java")

print(books)
print("Total Books =", len(books))
