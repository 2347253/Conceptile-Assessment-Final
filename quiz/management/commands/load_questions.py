import json
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Load questions from questions.json'

    def handle(self, *args, **kwargs):
        try:
            with open('questions.json', 'r') as file:
                questions = json.load(file)  # Load JSON data from the file
                for q in questions:
                    Question.objects.create(
                        question_text=q['question'],
                        option_a=q['A'],
                        option_b=q['B'],
                        option_c=q['C'],
                        option_d=q['D'],
                        correct_answer=q['answer']
                    )
                self.stdout.write(self.style.SUCCESS('Successfully loaded questions!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
