from django.shortcuts import render
import requests, json
import os

def home(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        past_responses = request.POST.get('past_responses', '')

        api_key = os.environ.get("GEMINI_API_KEY")
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": api_key
        }
        data = {
            "contents": [{"parts": [{"text": question}]}]
        }

        try:
            r = requests.post(url, headers=headers, data=json.dumps(data))
            if r.status_code == 200:
                res = r.json()
                response = res["candidates"][0]["content"]["parts"][0]["text"]
            else:
                response = f"Error {r.status_code}: {r.text}"
        except Exception as e:
            response = f"Exception: {e}"

        # Logic for past responses (better)
        if not past_responses:
            past_responses = response
        else:
            past_responses = f"{past_responses}<br/><br/>{response}"

        return render(request, 'home.html', {
            "question": question,
            "response": response,
            "past_responses": past_responses
        })

    return render(request, 'home.html', {"past_responses": ""})
