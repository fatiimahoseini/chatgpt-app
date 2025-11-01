from django.shortcuts import render, redirect
from django.contrib import messages
import requests, json
import os
from .models import Past

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

            # Save to DB (inside try)
            record = Past(question=question, answer=response)
            record.save()

        except Exception as e:
            response = f"Exception: {e}"

        # Handle past responses
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


def history(request):
    history = Past.objects.all()

    return render(request, 'history.html', {"history": history})

def delete_history(request, history_id):
    history = Past.objects.get(pk=history_id)
    history.delete()
    messages.success(request, ("Deleted successfully!"))
    return redirect('history')
