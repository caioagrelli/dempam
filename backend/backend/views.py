from django.http import HttpResponse

def test_view(request):
    return HttpResponse("rota de teste?")