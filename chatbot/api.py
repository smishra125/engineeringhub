from rest_framework.views import APIView
from rest_framework.response import Response

class ChatbotAPI(APIView):
    def post(self, request):
        question = request.data.get("question")
        return Response({
            "answer": f"AI response for: {question}"
        })
