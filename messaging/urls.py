
from django.urls import path
from .views import inbox, add_comment, toggle_like, add_reply


app_name = 'messaging'

urlpatterns = [
    path('like/<int:comment_id>/', toggle_like, name='toggle_like'),
    path('reply/<int:page_id>/<int:parent_id>/', add_reply, name='add_reply'),
    path('', inbox, name='inbox'),
    path('add/<int:page_id>/', add_comment, name='add_comment'),
]
