from django.urls import path

from main_app import views, admin_views, donor_views, receiver_views
from main_app.admin_views import donor_accept

urlpatterns = [

    path("dashboard",views.dashboard,name="dashboard"),
    path("login",views.Login,name="login"),
    path("DonorR",views.DonorR,name="DonorR"),
    path("ReceiverR",views.ReceiverR,name="ReceiverR"),
    path("",views.index, name="index"),
    path("login_view",views.Login_view,name="login_view"),


#admin
    path("admin_view",admin_views.admin_view,name="admin_view"),
    path("table",admin_views.table,name="table"),
    path('delete/<int:id>/',admin_views.remove,name="delete"),
    path('update/<int:id>/',admin_views.update,name="update"),
    path("table2",admin_views.table2,name="table2"),
    path('delete2/<int:id>/',admin_views.remove2,name="delete2"),
    path('update2/<int:id>/',admin_views.update2,name="update2"),
    path("req_admin",admin_views.req_admin,name="req_admin"),
    path("donor_accept",admin_views.donor_accept,name="donor_accept"),
    path('accept/<int:id>/', admin_views.accept, name="accept"),
    path('reject/<int:id>/', admin_views.reject, name="reject"),
    path("accept_view",admin_views.accept_view,name="accept_view"),
    path("reply_view",admin_views.reply_view,name="reply_view"),
    path("reply_feedback/<int:id>/",admin_views.reply_feedback,name="reply_feedback"),
    path("logou", admin_views.logou, name="logou"),


#donor
    path("donor_view", donor_views.donor_view, name="donor_view"),
    path("req_donor",donor_views.req_donor,name="req_donor"),
    path("donate/<int:id>",donor_views.donate,name="donate"),
    path("profile_donor", donor_views.profile_donor, name="profile_donor"),
    path('donor_update/<int:id>/', donor_views.donor_update, name="donor_update"),
    path("logou", donor_views.logou, name="logou"),

    #receiver
    path("receiver_view", receiver_views.receiver_view, name="receiver_view"),
    path("Receiver_req", receiver_views.Receiever_req, name="Receiver_req"),
    path('rmv/<int:id>/', receiver_views.rmv, name="rmv"),
    path("req_table",receiver_views.req_table,name="req_table"),
    path("feedbk", receiver_views.feedbk, name="feedbk"),
    path('reply', receiver_views.reply, name="reply"),
    path("profile_receiver", receiver_views.profile_receiver, name="profile_receiver"),
    path('receiver_update/<int:id>/', receiver_views.receiver_update, name="receiver_update"),
    path("logou", receiver_views.logou, name="logou"),

]


