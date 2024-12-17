import random
# from django.shortcuts import render
from django.http import JsonResponse
from .models import UserSession, Question, UserAnswer
from django.shortcuts import redirect, render
import re

def home(request):
    if request.method == "POST":
        username = request.POST.get("username").strip()
        
        if username:
            # Save the username in the session
            request.session["username"] = username
            print(f"Session set: {request.session['username']}")  # Debug log
            return redirect("start_quiz")
        else:
            return render(request, "quiz/home.html", {"error": "Name cannot be empty."})
    
    return render(request, "quiz/home.html")

from .models import UserSession

def start_quiz(request):
    username = request.session.get("username")  # Retrieve username from session
    print(f"Session username in start_quiz: {username}")  # Debug log

    if username:
        # Delete any existing sessions for the user
        UserSession.objects.filter(user=username).delete()
        print(f"Old sessions for user '{username}' deleted.")  # Debug log

        # Create a new UserSession for this quiz attempt
        session = UserSession.objects.create(user=username)
        print(f"New UserSession created: {session.id}")  # Debug log

        # Store the session ID in the request session
        request.session["session_id"] = session.id
        return render(request, "quiz/quiz.html", {"username": username})
    else:
        print("Redirecting to home because username is not in session")
        return redirect("home")


def get_random_question(request):
    if request.method == 'GET':
        questions = list(Question.objects.all())
        if questions:
            question = random.choice(questions)
            return JsonResponse({
                'id': question.id,
                'question': question.question_text,
                'options': {
                    'A': question.option_a,
                    'B': question.option_b,
                    'C': question.option_c,
                    'D': question.option_d,
                }
            })
        else:
            return JsonResponse({'error': 'No questions available.'}, status=404)


def submit_answer(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)  
            session_id = request.session.get("session_id")  
            question_id = data.get('question_id')
            selected_option = data.get('selected_option')

            if not session_id:
                return JsonResponse({'error': 'No active session found.'}, status=400)

            print(f"Session ID: {session_id}, Question ID: {question_id}, Selected Option: {selected_option}")  # Debug log

            # Fetch the current session and question
            session = UserSession.objects.get(id=session_id)
            question = Question.objects.get(id=question_id)

            # Check if the selected option is correct
            is_correct = question.correct_answer == selected_option

            # Record the answer
            UserAnswer.objects.create(
                session=session,
                question=question,
                selected_option=selected_option,
                is_correct=is_correct
            )

            # Update session score if correct
            if is_correct:
                session.score += 1
                session.save()

            return JsonResponse({'is_correct': is_correct})
        except Exception as e:
            # print(f"Error in submit_answer: {str(e)}")  # Debug log
            return JsonResponse({'error': str(e)}, status=400)



def end_quiz(request):
    if request.method == 'GET':
        session_id = request.session.get("session_id")  # Get the current session ID
        if not session_id:
            return JsonResponse({'error': 'No active session found.'}, status=400)

        try:
            session = UserSession.objects.get(id=session_id)
            answers = UserAnswer.objects.filter(session=session)
            # Prepare the result data
            results = {
                'total_questions': answers.count(),
                'correct_answers': answers.filter(is_correct=True).count(),
                'incorrect_answers': answers.filter(is_correct=False).count(),
            }
            return render(request, "quiz/results.html", {"results": results})
        except UserSession.DoesNotExist:
            return redirect("home")
        except Exception as e:
            # print(f"Error in end_quiz: {str(e)}")  # Debug log
            return redirect("home")





