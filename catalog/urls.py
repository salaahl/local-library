from django.urls import path
from . import views

urlpatterns = [
    # read
    #1er paramètre : url, 2è : la vue, 3e (optionnel) : le nom de la route (qui pourra ensuite s'utiliser ainsi dans la vue : {% url 'index' %})
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(),
         name='author-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('my-books/',
         views.LoanedBooksByUserListView.as_view(),
         name='my-borrowed'),
    # create
    path('user/create/', views.create_user, name='user-create'),
    path('author/create/', views.create_author, name='author-create'),
    path('book/create/', views.create_book, name='book-create'),
    path('book/<uuid:pk>/renew/', views.renew_book, name='book-renew'),
    path('book/<uuid:pk>/return/', views.return_book, name='book-return'),
    path('book_instance/create/',
         views.create_book_instance,
         name='book_instance-create'),
    path('genre/create/', views.create_genre, name='genre-create'),
    # update
    path('author/<int:pk>/update/',
         views.AuthorUpdate.as_view(),
         name='author-update'),
    path('book/<int:pk>/update/',
         views.BookUpdate.as_view(),
         name='book-update'),
    path('book_instance/<int:pk>/update/',
         views.BookInstanceUpdate.as_view(),
         name='book_instance-update'),
    path('genre/<int:pk>/update/',
         views.GenreUpdate.as_view(),
         name='genre-update'),
    # delete
    path('author/<int:pk>/delete/',
         views.AuthorDelete.as_view(),
         name='author-delete'),
    path('book/<int:pk>/delete/',
         views.BookDelete.as_view(),
         name='book-delete'),
    path('book_instance/<int:pk>/delete/',
         views.BookInstanceDelete.as_view(),
         name='book_instance-delete'),
    path('genre/<int:pk>/delete/',
         views.GenreDelete.as_view(),
         name='genre-delete'),
]
