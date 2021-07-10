from django.urls import path
from . import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
 	path('music/',views.music,name='music'),
 	path('blog/',views.blog,name='blog'),   
 	path('contact/',views.contact,name='contact'),
 	path('login/',views.login,name='login'),
 	path('Register/',views.Register,name='Register'),
 	path('single/',views.single,name='single'),
 	path('forgot_password/',views.forgot_password,name='forgot_password'),
 	path('enter_otp/',views.enter_otp,name='enter_otp'),
 	path('store/',views.store,name='store'),
 	path('enter_email/',views.enter_email,name='enter_email'),
 	path('verify_forgot_otp',views.verify_forgot_otp,name='verify_forgot_otp'),
 	path('update_password/',views.update_password,name='update_password'),
 	path('logout/',views.logout,name='logout'),
 	path('change_password/',views.change_password,name='change_password'),
 	path('seller_index/',views.seller_index,name='seller_index'),
 	path('seller_change_password/',views.seller_change_password,name='seller_change_password'),
 	path('edit_profile/',views.edit_profile,name='edit_profile'),
 	path('seller_edit_profile/',views.seller_edit_profile,name='seller_edit_profile'),
 	path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
 	path('seller_view_product/',views.seller_view_product,name='seller_view_product'),
 	path('seller_product_detail/<int:pk>/',views.seller_product_detail,name='seller_product_detail'),
 	path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
 	path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
	path('user_view_product/<str:pb>/',views.user_view_product,name='user_view_product'),
	path('user_product_detail/<int:pid>/',views.user_product_detail,name='user_product_detail'),
	path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
	path('mywishlist/',views.mywishlist,name='mywishlist'),
	path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
	path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
	path('mycart/',views.mycart,name='mycart'),
	path('remove_cart/<int:pk>/',views.remove_cart,name='remove_cart'),
	path('change_qty/',views.change_qty,name='change_qty'),
	
]
	