
from django.contrib import admin
from django.urls import path
from Blog.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name = 'home'),
    path('about/',About,name = 'about'),
path('contact/',Contact,name = 'contact'),
path('login/',Login,name = 'login'),
path('signup/',Signup,name = 'signup'),
path('myblog/',MyBlog,name = 'blogs'),
path('logout/',Logout_user,name = 'logout'),
path('changeImage/',Chenge_image,name = 'change_i'),
path('changepwd/',Change_password,name = 'change_p'),

path('Add_blog/',Add_Blog,name = 'add_blog'),
    path('blog_detail/<int:bid>',Blog_detail,name='detail'),
path('category_detail/<int:cid>',Category_detail,name='c_detail'),
path('blog_delete/<int:pid>',Delete_post,name='delete'),
path('blog_like/<int:pid>',LikeThePost,name='like'),
path('blog_comment/<int:pid>',CommentThePost,name='comment'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
