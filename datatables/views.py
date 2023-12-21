from django.urls import reverse
from django.shortcuts import render
from django.http import JsonResponse

from django_jquery_datatables.utils import JqueryDatatable

from .serializers import DataSerializer
from .models import Datatable


def datatable_json(request):
    queryset = Datatable.objects.all()
    # You can also sort the initial data here.
    return JqueryDatatable(request, queryset, DataSerializer)


def datatables_page(request):
    return render(
        request,
        'datatables/datatables.html',
        {
            'urls': {
                'add_to_cart_url': reverse('add_to_cart'),
                'data_url': reverse('data'),
            }
        }
    )


def add_to_cart(request):
    resp_success = {'success': True, 'message': 'Данные приняты'}
    resp_error = {'success': False, 'message': 'Произошла ошибка'}
    try:
        id = request.POST['id']
        count = request.POST['count']
        resp_success['message'] += f' {id=} {count=}'
        return JsonResponse(resp_success)
    except Exception as e:
        print(e)
        return JsonResponse(resp_error)
