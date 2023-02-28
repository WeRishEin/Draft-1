from django.http import JsonResponse
import csv
import requests

def get_csv_data():
    url = 'http://ctdbase.org/detail/go?type=disease&acc=MESH%3AD008579&view=gene&format=csv'
    response = requests.get(url)
    csv_data = response.content.decode('utf-8')
    reader = csv.DictReader(csv_data.splitlines())
    return list(reader)

class CsvDataViewSet(viewsets.ViewSet):
    def list(self, request):
        csv_data = get_csv_data()
        return JsonResponse(csv_data, safe=False)
