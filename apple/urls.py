"""apple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from core import views
from upload.forms import BookForm
from upload import views as upviews #views from upload app
from django.conf import settings
from django.conf.urls.static import static
from sstudy import views as sviews
from assignment import views as aviews
from sassignments import views as vviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('secret/',views.secret_page,name='secret'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('upload/',upviews.book_list,name='upload'),
    path('upload/<int:pk>/', upviews.delete_book, name='delete'),
    path('student_StudyMaterial/',sviews.sbook_list, name='studymaterial'),
    path('student_home/',sviews.student_home, name='shome'),
    path('assignment_upload/',aviews.assignment_upload, name='assignment'),
    path('assignment_upload/<int:pk>/', aviews.delete_assignment, name='assignment_delete'),
    path('view_assignment/',vviews.view_ass, name='view'),
    path('upload_solution/',vviews.upload_solution, name='solution'),
    path('view_solution/',aviews.view_ass, name='ViewSolution'),
    path('upload_solution/<int:pk>/',aviews.delete_solution, name='DeleteSolution'),
    path('upload/file/',upviews.upload_book,name='upfile'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
