from django.contrib import admin
from .models import Book, Author, Comments, Booking
from import_export.admin import ImportExportModelAdmin


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'get_comments', 'publication_date', 'count', 'author', 'create_date')
    list_display_links = ('id', 'title', 'description', 'price', 'get_comments', 'publication_date', 'count', 'author')
    search_fields = ('id', 'title')
    ordering = ('title',)

    def get_comments(self, obj):
        
        return obj.comments.count()


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('text', 'student')
    


@admin.register(Booking)
class BookingAdmin(ImportExportModelAdmin):
    list_display = ('id', 'book', 'student', 'take_date', 'returned_date')

    def get_book_title(self, obj):

        return obj.book.title

    def get_student_name(self, obj):
        
        return "Student Name (Replace with logic to retrieve student name)"

    list_display = ('id', 'get_book_title', 'get_student_name', 'take_date', 'returned_date')
