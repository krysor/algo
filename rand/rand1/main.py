from hire_assistant import hire_assistant
import random

number_candidates = 10;
candidates = [random.randint(1, 100) for _ in range(number_candidates)]
print("candidates: ", candidates);

hire_assistant(candidates);