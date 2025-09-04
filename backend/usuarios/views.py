from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Ferramenta de segurança do Django

# View para a Homepage
def homepage(request):
    return render(request, 'usuarios/homepage.html')

# View para a página administrativa
@login_required # <-- ESTE É O "SEGURANÇA" NA PORTA
def pagina_administrativa(request):
    # Primeiro, crie o arquivo HTML para esta página
    # em 'backend/usuarios/templates/usuarios/pagina_administrativa.html'
    return render(request, 'usuarios/pagina_administrativa.html')