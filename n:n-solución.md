# SOLUCIÓN EJERCICIO RELACIONES (N:N)
Para empezar tienes que tener en cuenta que cuando tu pidas la lista de autores de un libro, no te dará los nombres, sino los id de cada autor. Si quisieras saber a quien pertenece el id deberas de hacer un select en la tabla de autores con condición de que el id sea al menos igual a alguno de los que hace referencia el libro. Para conseguir la lista de autores asociados debes usar esta sentencia SQL en la terminal con la BD abierta:

- *select * from my_first_app_book_author;*

Si no has sabido como asociar los autores, aquí dejo un ejemplo de como recuperar un libro ya creado, como crear autores y como he asociado dichos autores a ese libro en concreto:

    #Importando los modelos libro, autores,
    from my_first_app.models import Book, Author

    #Obtención del libro creado antes en el curso
    book = Book.objects.first()

    #Creación de dos autores, pese a que esta novela solo tiene uno originalmente
    patrick = Author(name="Patrick Rothfuss", birthday="1973-06-06")
    patrick.save
    emily = Author(name="Emily Robbinson", birthday="1974-06-25")
    emily.save()

    #Creación de una lista para asociarla al libro
    authors_list = [patrick, emily]

    #Asociación de la lista con el libro
    book.authors.set(authors_list)
    book.save()