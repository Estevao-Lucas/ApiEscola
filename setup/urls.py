from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from escola.views import AlunosViewSet, CursoViewSet, ListaAlunosMatriculados, MatriculaViewSet, ListaMatriculasAlunos
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matricula', MatriculaViewSet, basename='Matriculas')


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAlunos.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]  
