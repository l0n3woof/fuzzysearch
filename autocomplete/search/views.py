from django.shortcuts import render
from django.http import JsonResponse

from operator import itemgetter
from autocomplete import word_dict

word_list = [(k,v) for k,v in word_dict.items()]
sort_dict = sorted(word_list,key=itemgetter(1), reverse=True)

def search(request):
    res = []
    contain_list = []
    word = request.GET.get('word')
    c = 0
    try:
        word_dict[word.lower()]
        res.append(word)
        c += 1
    except KeyError:
        pass
    for i in word_list:
        i = i[0]
        if i.lower()==word.lower():
            continue
        if i.lower().startswith(word.lower()):
            res.append(i)
            c += 1
        elif word.lower() in i.lower():
            contain_list.append(i)
        if c==25:
            break
    res_len = len(res)
    if res_len == 25:
        return JsonResponse({'result': res})
    else:
        remain_len = 25 - res_len
        res.extend(contain_list[0:remain_len])
    return JsonResponse({'result': res})
