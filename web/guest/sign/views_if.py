from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError

def add_event(request):
    eid = request.POST.get('eid', '')
    name = request.POST.get('name', '')
    limit = request.POST.get('limit', '')
    status = request.POST.get('status', '')
    address = request.POST.get('address', '')
    # start_time = request.POST.get('start_time', '')

    if eid == '' or name == '' or limit == '':
        return JsonResponse({'status':10021, 'message':'parameter error'})
    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address,
                             status=int(status))
    except:
        pass
    return JsonResponse({'status': 200, 'message':'add event success'})

from django.core.exceptions import ValidationError, ObjectDoesNotExist

def get_event_list(request):
    eid = request.GET.get('eid', '')
    name = request.GET.get('name', '')
    print('eid:',eid, name)
    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':10022, 'message':'query is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            # event['start_time'] = result.start_time
            return JsonResponse({'status':200, 'message':'success', 'data': event})
    else:
        return JsonResponse({'status':10022, 'message':'query empty'})

def user_sign(request):
    pass

