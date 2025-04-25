from typing import override
from django.http import JsonResponse
from rest_framework.views import APIView
from abc import ABC, abstractmethod
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    get=extend_schema(exclude=True),
    post=extend_schema(exclude=True),
    put=extend_schema(exclude=True),
    delete=extend_schema(exclude=True),
)
@method_decorator(csrf_exempt, name='dispatch')
class AbstractDynamicView(APIView, ABC):
    def dispatch(self, request, *args, **kwargs):
        self.routeParameter = kwargs.get('routeParameter')
        return super().dispatch(request)
    
    @abstractmethod
    def get(self, request):
        pass

    @abstractmethod
    def post(self, request):
        pass

    @abstractmethod
    def put(self, request):
        pass

    @abstractmethod
    def delete(self, request):
        pass


@extend_schema(
    methods=["GET", "POST", "PUT", "DELETE"],
    tags=["DynamicView"],
    description="View sem parâmetro de rota"
)
class DynamicViewNoParam(AbstractDynamicView):
    @override
    def get(self, request):
        return returnProperMessage("GET", self.routeParameter)
    
    @override
    def post(self, request):
        return returnProperMessage("POST", self.routeParameter)
    
    @override
    def put(self, request):
        return returnProperMessage("PUT", self.routeParameter)
    
    @override
    def delete(self, request):
        return returnProperMessage("DELETE", self.routeParameter)


@extend_schema(
    methods=["GET", "POST", "PUT", "DELETE"],
    tags=["DynamicView"],
    description="View com parâmetro de rota"
)
@method_decorator(csrf_exempt, name='dispatch')
class DynamicViewWithParam(AbstractDynamicView):
    @override
    def get(self, request):
        return returnProperMessage("GET", self.routeParameter)
    
    @override
    def post(self, request):
        return returnProperMessage("POST", self.routeParameter)
    
    @override
    def put(self, request):
        return returnProperMessage("PUT", self.routeParameter)
    
    @override
    def delete(self, request):
        return returnProperMessage("DELETE", self.routeParameter)


@method_decorator(csrf_exempt, name='dispatch')
def returnProperMessage(method: str, routeParameter: str = None):
    if routeParameter is None:
        return JsonResponse({"message": f"{method} sem param"})
    else:
        return JsonResponse({"message": f"{method} com param: {routeParameter}"})