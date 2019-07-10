from django.urls import path



from .views import (
            ProductListView, 
            # product_list_view, 
            # ProductDetailView, 
            # product_detail_view,
            # ProductFeaturedDetailView,
            # ProductFeaturedListView,
            ProductDetailSlugView
        )

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    # path('featured/', ProductFeaturedListView.as_view()),
    # path('products-fbv/', product_list_view),
    # path('products/<int:pk>', ProductDetailView.as_view()),
    path('<str:slug>/', ProductDetailSlugView.as_view(), name='detail'),
    # path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    # path('products-fbv/<int:pk>', product_detail_view),
]
