from django.shortcuts import render

# Create your views here.
# from django.http import JsonResponse
# # from .models import WellData
# from .serializers import DataSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status


# def data_list(request,format=None):
#     if request.method =='GET':
#         data= WellData.objects.all()
#         serializer= DataSerializer(data,many=True)
#         return Response({'data': serializer.data})

import pandas as pd
from django.http import JsonResponse
# from .models import WellData

# def load_data(request):
#     file_path = 'data.xls'
#     df = pd.read_excel(file_path)
#     for _, row in df.iterrows():
#         api_well_number = str(row['API WELL  NUMBER'])
#         for quarter in range(1, 5):
#             oil = row[f'Q{quarter} OIL']
#             gas = row[f'Q{quarter} GAS']
#             brine = row[f'Q{quarter} BRINE']
#         WellData.objects.create(
#                 api_well_number=api_well_number,
                
#                 oil=oil,
#                 gas=gas,
#                 brine=brine
#             )
#     return JsonResponse({'message': 'Data loaded successfully.'})
