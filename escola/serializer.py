from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


#Responsável por fazer a ponte da API
#--> Tranforma em JSON 
#Transforma em Python pro banco de dados <--
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = [] #funciona igual o __all__ 

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao') #mostra o nome do curso
    periodo = serializers.SerializerMethodField() #mostra o periodo do curso por meio de um metodo
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj): #metodo que mostra o periodo do curso
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno']