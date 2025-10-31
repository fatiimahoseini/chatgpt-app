from django.shortcuts import render
import requests, json

def home(request):
    if request.method == 'POST':
        question = request.POST.get('question')

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": "AIzaSyC8ayLaWVhKks922ajbT-8cRSJ0qkN48gM"
        }
        data = {
            "contents": [{"parts": [{"text": question}]}]
        }

        try:
            r = requests.post(url, headers=headers, data=json.dumps(data))
            if r.status_code == 200:
                res = r.json()
                answer = res["candidates"][0]["content"]["parts"][0]["text"]
            else:
                answer = f"Error {r.status_code}: {r.text}"
        except Exception as e:
            answer = f"Exception: {e}"

        return render(request, 'home.html', {"question": question, "response": answer})

    return render(request, 'home.html', {})
