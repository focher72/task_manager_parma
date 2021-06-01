from oracle_base import models, serializers
from django.conf import settings
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
import requests
import json


def create_client(request):
    func_success = True
    account = request.GET.get('account').split()
    if account is None:
        return JsonResponse({'success': False,
                             'func_result': 'give my account blyat'})
    else:
        create_accout_info = []

        for account_elnt in account:
            param = {"mnemo": "GetUser", "secret": "228", "args": {"lic_number": account_elnt}}
            try:
                json_param = json.dumps(param)
                res = requests.post(settings.PARMATEL_BILLING, data=json_param).json()

                if res["result"][0]["Ctitle"]:
                    res_type = True
                    fio = res["result"][0]["Ctitle"]
                else:
                    res_type = False
                    fio = res["result"][0]["Csurname"] + " " + \
                        res["result"][0]["Cname"] + " " + \
                        res["result"][0]["Cpatronymic"]

            except IndexError:
                func_success = False
                result_func = "{} -> API problem(not found)".format(account_elnt)
                create_accout_info.append(result_func)
                break

            if models.Client_lists.objects.filter(account=res["result"][0]["Clic_number"]).count() == 0:
                models.Client_lists.objects.create(
                    account=res["result"][0]["Clic_number"],
                    clnt_type=res_type,
                    clnt_name=fio,
                    abonent_adr="",
                    inn=res["result"][0]["Cinn"],
                    email=res["result"][0]["Cemail"],
                    contact=res["result"][0]["Ccontact_phone1"]
                )
                result_func = "{} -> create user".format(res["result"][0]["Clic_number"])
            else:
                result_func = "{} -> user found in the database, not created".format(res["result"][0]["Clic_number"])
                func_success = False

            create_accout_info.append(result_func)

        context = {
            'success': func_success,
            'func_result': create_accout_info
        }

        return JsonResponse(context, content_type='text/plain; charset=utf-8')


class ClientListSet(viewsets.ReadOnlyModelViewSet):
    """Полная информация о всех заявках"""
    queryset = models.Client_lists.objects.all()
    serializer_class = serializers.ClientListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ['clnt_type']
    search_fields = ['clnt_name', 'abonent_adr']
    ordering_fields = ['clnt_name', 'abonent_adr']
    permission_classes = [permissions.IsAuthenticated]


class ClientShpdInfoSet(viewsets.ReadOnlyModelViewSet):
    """Полная информация о всех заявках"""
    queryset = models.Client_shpd_info.objects.all()
    serializer_class = serializers.ClientShpdInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
