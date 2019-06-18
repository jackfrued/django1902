from functools import wraps

from django.http import JsonResponse
from django.shortcuts import redirect

LOGIN_REQUIRED_URLS = {
    '/praise/', '/criticize/', '/pdf/', '/excel/', '/bar/1', '/bar/2',
    '/teachers_data/', '/subjects_data/'
}


def check_login_middleware(get_resp):

    @wraps(get_resp)
    def wrapper(request, *args, **kwargs):
        if request.path in LOGIN_REQUIRED_URLS:
            if 'userid' in request.session:
                return get_resp(request, *args, **kwargs)
            else:
                if request.is_ajax():
                    return JsonResponse({'code': 10003, 'hint': '请先登录'})
                else:
                    backurl = request.get_full_path()
                    return redirect(f'/login/?backurl={backurl}')
        return get_resp(request, *args, **kwargs)

    return wrapper
