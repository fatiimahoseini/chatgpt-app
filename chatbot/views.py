from django.shortcuts import render

# Create HomePage
def home(request):
  # Check for form submission
  if request.method == 'POST':
    question = request.POST.get('question')
    return render(request, 'home.html', {"question": question})
  return render(request, 'home.html', {})
