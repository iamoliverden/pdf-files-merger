
# views.py

from django.shortcuts import render
from django.http import JsonResponse
import os
from PyPDF2 import PdfMerger
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def merger_app(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            folder_path = data.get('folder_path')
            output_path = data.get('output_path')

            if not folder_path or not output_path:
                return JsonResponse({'status': 'error', 'message': 'Folder path and output path are required.'})

            print(f"Folder Path: {folder_path}")
            print(f"Output Path: {output_path}")

            merger = PdfMerger()
            pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

            # Sort files by name
            pdf_files.sort()

            for filename in pdf_files:
                file_path = os.path.join(folder_path, filename)
                merger.append(file_path)

            # Simplify the output path
            output_file_path = os.path.join(output_path, 'merged.pdf')
            print(f"Output File Path: {output_file_path}")

            merger.write(output_file_path)
            merger.close()

            return JsonResponse({'status': 'success', 'message': 'PDFs merged successfully!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data.'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
