from io import BytesIO
from base64 import b64encode, b64decode
from django.http.response import HttpResponseRedirect
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_pdf.renderer import PDFRenderer
from drf_pdf.response import PDFResponse
from reports.models import Reports
from reports.serializers import ReportsList


class ReportsView(ViewSet):    
    
    def list(self, request):
        queryset = Reports.objects.all()
        serializer = ReportsList(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk):
        return HttpResponseRedirect(redirect_to='/report/'+pk)

    def create(self, request):
        '''
            Simple Custom Save Method
        '''
        title_file = request.data.get('title')
        str_b64_file = request.data.get('file')
        
        if not (title_file and str_b64_file):
            return Response('Missing Data.')
            
        i_Reports = Reports(
            title=title_file,
            file=b64encode(b64decode(str_b64_file))
        ).save()

        return Reports('Data saved.')


class ReportsLoadPDF(ViewSet):

    renderer_classes = (PDFRenderer, ) # !important

    def retrieve(self, request, pk):
        queryset = Reports.objects.filter(id=pk).get()
        
        bytes = b64decode(queryset.file, validate=True)
        
        pdf = BytesIO(bytes) # Simulating File

        return PDFResponse(
            pdf.getvalue(),
            file_name=queryset.title,
            template_name=queryset.title,
            status=status.HTTP_200_OK
        )  
