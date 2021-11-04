from django.shortcuts import render
from django.http.response import HttpResponse

from q7.forms import AlvoForm
from q7.models import Alvo
import json


# Create your views here.
def homepage(request):
    
    context1 = {
        'alvo_form': AlvoForm
    }

    return render(request, 'q7_home.html', context1)

def ajax_create_alvo(request):

    if request.is_ajax() and request.method == "POST":
        #alvo_data = json.loads( request.POST['data'] )
        alvo_data = request.POST
        print(alvo_data['nome'])
        new_alvo = Alvo()

        new_alvo.nome = alvo_data['nome']
        new_alvo.latitude = alvo_data['latitude']
        new_alvo.longitude = alvo_data['longitude']
        new_alvo.expiration_date = alvo_data['expiration_date']

        new_alvo.save()
    
    return HttpResponse(new_alvo.pk,content_type="text/html",status=200)


def ajax_update_alvo(request, pk):
   
    #chegou ate aqui        
    if request.is_ajax() and request.method == "POST":
        print('\nAlvo vai ser atualizado\n')
        old_alvo = Alvo.objects.get(id=pk)
        alvo_data = request.POST
        print(alvo_data)

        old_alvo.nome = alvo_data['nome']        
        old_alvo.latitude = alvo_data['latitude']
        old_alvo.longitude = alvo_data['longitude']
        old_alvo.expiration_date = alvo_data['expiration_date']

        old_alvo.save()

    return HttpResponse(status=200)

def ajax_delete_alvo(request, pk):

    if request.is_ajax():
        print('Deletar Alvo')
        Alvo.objects.get(id=pk).delete()

    return HttpResponse(status=200)

