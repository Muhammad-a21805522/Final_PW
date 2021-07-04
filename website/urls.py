from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path('multi', views.multi_page_view, name='multi'),
    path('amb', views.amb_page_view, name='amb'),
    path('dif', views.dif_page_view, name='dif'),
    path('form', views.form_page_view, name='form'),
    path('tecnicas', views.tecnicas_page_view, name='tecnicas'),
    path('inventario', views.inventario_page_view, name='inventario'),
    path('apresentacao', views.apresentacao_page_view, name='apresentacao'),
    path('intro', views.intro_page_view, name='intro'),
    path('', views.intro_page_view, name='intro'),
    path('contacto', views.contactos_page_view, name='contacto'),
    path('addContacto', views.nova_tarefa_view, name='addContacto'),
    path('editContacto/<int:contacto_id>', views.edita_tarefa_view, name='editContacto'),
    path('apaga/<int:contacto_id>', views.apaga_tarefa_view, name='apaga'),
    path('login/', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('comentarios', views.comentarios_page_view, name="comentarios"),
    path('resultadoComentarios', views.resultadoComentarios_page_view, name="resultadoComentarios"),
    path('resultadoQuizz', views.resultadosQuizz_page_view, name="resultadoQuizz"),
    path('spa', views.spa_page_view, name="spa"),
    path("sections/<int:num>",views.section_page_view, name="section")
]
