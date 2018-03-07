from django.http import HttpResponseRedirect

need_login = ['/', ]


class AuthMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path in need_login:
            cid = request.COOKIES.get('cid')
            if not cid:
                return HttpResponseRedirect('/login/')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response