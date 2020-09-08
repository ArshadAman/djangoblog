
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


admin.site.site_header="Mad About Hacking Admin Panel"
admin.site.site_title="MAH Administration"
admin.site.index_title="Welcome to MAH Admin Panel"
from blog.sitemaps import PostSitemap
from django.contrib.sitemaps.views import sitemap



sitemaps = {
    "posts": PostSitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
    path('course/',include('course.urls')),
    path('ebook/',include('ebook.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('ckeditor/', include(
        'ckeditor_uploader.urls')),
        # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset'),
]+ static(settings.MEDIA_URL, 
           document_root=settings.MEDIA_ROOT)

