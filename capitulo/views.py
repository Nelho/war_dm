from django.shortcuts import render, HttpResponseRedirect
from capitulo.forms import CapituloUserForm, FormularioForm
from main.models import *
from capitulo.models import UsuarioCapitulo


def cadastrarCapitulo(request):
    if(request.method == 'POST'):
        form = CapituloUserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            nomeCap = form.cleaned_data['nomeCap']
            password = form.cleaned_data['password']
            numero = form.cleaned_data['numero']
            user = User(username='Cap_'+str(numero), first_name=nomeCap , password=password,
                        email='capitulo_'+str(numero)+'@demolaypb.com.br')
            user.save()

            regiao = form.cleaned_data['regiao']
            usuario = Usuario(user=user, regiao=regiao, tipoUsuario='CAP')
            usuario.save()

            telefone = form.cleaned_data['telefone']
            Contato(usuario=user, contato=telefone)

            avaliador = form.cleaned_data['avaliador']
            dataFundacao = form.cleaned_data['dataFundacao']
            dataInstacao = form.cleaned_data['dataInstalacao']
            mestreConsenheiro = form.cleaned_data['mestreCosenheiro']
            usuarioCap = UsuarioCapitulo(numero=numero, dataFundacao=dataFundacao, dataInstalacao=dataInstacao,
                                         mestreConselheiro=mestreConsenheiro, avaliador=avaliador, usuarioCap=usuario)
            usuarioCap.save()
        return HttpResponseRedirect('/capitulo/cadastro/')
    form = CapituloUserForm()
    context = {"form" : form}
    return render(request, 'capitulo/cadastroCapitulo.html', context=context)

def cadastrarFormulario(request):
    if(request.method=="POST"):
        form = FormularioForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            resumo = form.cleaned_data['resumo']
            planejamento = form.cleaned_data['planejamento']
            abrangencia = form.cleaned_data['abrangencia']
            resultado = form.cleaned_data['resultado']
            
            dataRealizacao = form.cleaned_data['dataRealizacao']
            zip_formulario = request.FILES('documentos')
            relatorio = Formulario(resumo = resumo, planejamento = planejamento, abrangencia = abrangencia, resultado = resultado, dataRealizacao = dataRealizacao, zip_formulario = documentos)
            relatorio.save()

    form = FormularioForm()
    context = {"form":form}
    return render(request, 'capitulo/relatorio_form.html', context= context)