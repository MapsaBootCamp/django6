from django.shortcuts import render
from django.views import View


class ResumeView(View):

    # def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
    #     self.user_course = None
    #     if request.user.is_authenticated:
    #     delf.request
    #     return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "resume/index.html")