# -*- coding: utf-8 -*-

'''
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   kbqa_server.py
 
@Time    :   2020/3/9 9:57 上午
 
@Desc    :
 
'''

from django.http import JsonResponse
import json
import logging
import datetime

from Chatbot_KG_rest.Api.bot.kbqa_predict import get_answer

logger = logging.getLogger(__name__)


def kbqa_server(request):
    if request.method == 'POST':

        try:
            jsonData = json.loads(request.body.decode('utf-8'))
            msg = jsonData["msg"]
            localtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = get_answer(msg)
            dic = {
                "desc": "Success",
                "ques": msg,
                "result": result,
                "time": localtime
            }
            log_res = json.dumps(dic, ensure_ascii=False)
            logger.info(log_res)
            return JsonResponse(dic)
        except Exception as e:
            logger.info(e)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)