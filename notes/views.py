from django.http import JsonResponse

NOTES = [
    {"id": 1, "title": "Buy groceries", "content": "Milk, eggs, bread"},
    {"id": 2, "title": "Learn Django", "content": "Build a GET API using a Python list"},
    {"id": 3, "title": "Walk the dog", "content": "30 minutes in the park"}
]

def get_notes(request):
    if request.method == "GET":
        return JsonResponse({"notes": NOTES})
    return None

def health_check(request):
    return JsonResponse(
        data={
            "status": "healthy",
            "message": "Server is awake!"
        },
        status=200
    )