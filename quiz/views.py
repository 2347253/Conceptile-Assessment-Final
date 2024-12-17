from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Question, UserAnswer
import random, json


# Home View: Displays the homepage and validates the placeholder input
def home(request):
    if request.method == "POST":
        user_input = request.POST.get("username", "").strip()
        if user_input.lower() == "start":  # Check if the input is 'start'
            return redirect("start_quiz")  # Redirect to the start quiz page
        else:
            return render(request, "quiz/home.html", {"error": "Type 'start' to proceed."})

    return render(request, "quiz/home.html")


# Start Quiz View: Loads the quiz.html page
def start_quiz(request):
    return render(request, "quiz/quiz.html")


# Fetch Random Question View: Fetches a random question from the database
def get_random_question(request):
    if request.method == "GET":
        questions = list(Question.objects.all())
        if questions:
            question = random.choice(questions)  # Pick a random question
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
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"Request Body: {request.body}")  # Debugging log
            print(f"Parsed Data: {data}")

            question_id = data.get('question_id')
            selected_option = data.get('selected_option')

            if not question_id or not selected_option:
                return JsonResponse({'error': 'Invalid data: question_id and selected_option are required'}, status=400)

            # Retrieve the question and validate the answer
            question = Question.objects.get(id=question_id)
            is_correct = question.correct_answer == selected_option

            # Save the answer (no session required now)
            UserAnswer.objects.create(
                question=question,
                selected_option=selected_option,
                is_correct=is_correct
            )

            print(f"Question ID: {question_id} Selected Option: {selected_option}")
            print(f"Is Correct: {is_correct}")

            return JsonResponse({'is_correct': is_correct, 'success': True})
        except Question.DoesNotExist:
            return JsonResponse({'error': 'Question not found.'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

# End Quiz View: Displays the results of the user's quiz attempt
def end_quiz(request):
    if request.method == "GET":
        answers = UserAnswer.objects.all()  # Fetch all user answers
        total_questions = answers.count()
        correct_answers = answers.filter(is_correct=True).count()
        incorrect_answers = total_questions - correct_answers

        # Clear UserAnswer table for the next attempt
        UserAnswer.objects.all().delete()

        return render(request, "quiz/results.html", {
            "results": {
                "total_questions": total_questions,
                "correct_answers": correct_answers,
                "incorrect_answers": incorrect_answers,
            }
        })
