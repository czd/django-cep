# -*- coding: utf-8 -*-
# @Author: czd
# @Date:   2017-05-20 11:38:51
# @Last Modified by:   czd
# @Last Modified time: 2017-05-20 12:23:05


# -*- coding: utf-8 -*-
from django.http import JsonResponse
import urllib2
import re
import json

def cep(numero):
    url = 'http://viacep.com.br/ws/%s/json/' % str(numero)
    resp = urllib2.urlopen(url)
    return json.load(resp)

def addressGet(request, zipcode):
    zipcode = re.sub('[^\d]+', '', zipcode)
    results = cep(zipcode)
    return JsonResponse(results)
