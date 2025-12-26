from django.shortcuts import render
import openai
from django.http import JsonResponse

def ask_ai(request):
    question = request.GET.get("q")
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return JsonResponse({"answer": response.choices[0].message["content"]})

