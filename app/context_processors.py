from django.contrib.auth import get_user_model

def auth_context_processor(request):
    User = get_user_model()
    user = request.user if request.user.is_authenticated else None
    return {'user': user}