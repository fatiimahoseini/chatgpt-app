from django.shortcuts import render

# Create HomePage
def home(request):
  return render(request, 'chatbot/home.html', {})
