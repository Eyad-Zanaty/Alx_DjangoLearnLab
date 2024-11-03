book01 = Book(title='1984', author='George Orwell', publication_year= 1949)
# Adding book to the model bookshelf in the class Book with title='1984', author='George Orwell', publication_year= 1949

Book.objects.all()
# Retrive the all books

Book.objects.filter(author= 'George Orwell').delete()
# Delete the book with author George Orwell

Book.objects.filter(author= 'George Orwell').update(title='Nineteen Eighty-Four')
# Update the book written by an author called George Orwell to have a new title called Nineteen Eighty-Four