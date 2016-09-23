# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json
from django.core import serializers
from django.db.models.query import QuerySet
from django.db import models
from django.core import serializers
from mysite.models import Gzzb3
from mysite.models import Gzzb4
from mysite.models import Mima
# from books.models import Gzzb3
# from books.models import Mima
from django.shortcuts import render
import datetime
import MySQLdb


def hello(request):
    return HttpResponse("Hello world")


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})


def book_list(request):
    db = MySQLdb.connect(user='root', db='mydb', passwd='root', host='localhost')
    cursor = db.cursor()
    cursor.execute("SELECT address FROM bookb_publisher where name='Apress'")
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('current_datetime.html', {'current_date': names})


def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = str(request.GET['q'])
        sj = request.GET['sj']
        m = request.GET['m']
        m2 = Mima.objects.filter(mimaxm__exact=q)
        if any(m2) == True:
            if Mima.objects.get(mimaxm__exact=q).mimamm == m:
                if int(sj) < 201602:
                    #        books = Publisher.objects.filter(name__icontains=q)
                    books = Gzzb3.objects.filter(gz38__exact=q).filter(gz1__contains=sj).order_by("-gz1").values()
                    #        qwe = Publisher._meta.fields
                    return render_to_response('search_results.html', {'books': books, 'query': q})
                else:
                    qwe = Gzzb4._meta.fields
                    books = list(
                        Gzzb4.objects.filter(gz4_5__exact=q).filter(gz4_73__contains=sj).order_by("-gz4_73").values(
                            'gz4_73', 'gz4_2', 'gz4_4', 'gz4_5', 'gz4_13', 'gz4_14', 'gz4_18', 'gz4_19', 'gz4_25',
                            'gz4_24', 'gz4_23', 'gz4_22', 'gz4_21', 'gz4_20', 'gz4_47', 'gz4_17', 'gz4_27', 'gz4_34',
                            'gz4_33', 'gz4_43', 'gz4_44', 'gz4_48', 'gz4_49', 'gz4_50', 'gz4_51', 'gz4_52', 'gz4_53',
                            'gz4_54', 'gz4_55', 'gz4_56', 'gz4_57', 'gz4_58', 'gz4_59', 'gz4_10', 'gz4_63', 'gz4_66',
                            'gz4_67', 'gz4_70', ))
                    data = json.dumps(books)
                    return render_to_response('search_results2.html', {'books': data, 'query': q})
            else:
                return HttpResponse('密码错误。')
        else:
            return HttpResponse('姓名不存在或有误。')
    else:
        return HttpResponse('请输入信息。')


def home(request):
    query = ['戴奇凯']
    btsz = ['gz4_1', 'gz4_2', 'gz4_3', 'gz4_4', 'gz4_5']
    books = list(Gzzb3.objects.filter(gz38__exact='戴奇凯').filter(gz1__contains='20151').order_by("-gz1").values(
        'gz1',
        'gz36',
        'gz37',
        'gz38',
        'gz39',
        'gz49',
        'gz13',
        'gz54',
        'gz55',
        'gz79',
        'gz80',
        'gz81',
        'gz82',
        'gz69',
        'gz58',
        'gz59',
        'gz26',
        'gz57',
        'gz14',
        'gz15',
        'gz16',
        'gz18',
        'gz20',
        'gz22',
        'gz24',
        'gz61',
        'gz17',
        'gz65',
        'gz66',
        'gz31',
        'gz3',
        'gz4',
        'gz12',
        'gz53',
        'gz60',
        'gz25',
        'gz5',
        'gz7',
        'gz56',
        'gz48', ))
    data = json.dumps(books)
    qwe = Gzzb3._meta.fields
    #    books = serializers.serialize("json", books2)
    return render_to_response('qw.html',
                              {'books': data,
                               'query': query})


def home2(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'home.html', {
        'List': json.dumps(List),
        'Dict': json.dumps(Dict)
    })
