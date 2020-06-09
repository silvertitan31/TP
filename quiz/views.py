from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from quiz.models import Quiz
from quiz.serializers import QuestionSerializer

# Create your views here.
@csrf_exempt
def question_list(request):
    """
    List all question snippets.
    """
    if request.method == 'GET':
        questions = Quiz.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

def question_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        question = Quiz.objects.get(pk=pk)
    except Quiz.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data)

    