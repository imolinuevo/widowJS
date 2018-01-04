from django.urls import include, path
import presenter.views.use_case1 as use_case1
import presenter.views.use_case2 as use_case2

urlpatterns = [
    path('', use_case1.index),
    path('use_case1', use_case1.index),
    path('use_case2', use_case2.index),
]