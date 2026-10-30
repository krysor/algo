# from hire_assistant import hire_assistant
# import random

# multiplier = 10

# def test_input_size(input_size: int):
#     number_candidates = input_size;
#     candidates = [  
#         random.randint(1, multiplier * number_candidates)
#         for _ in range(number_candidates)
#     ]    
#     return hire_assistant(candidates);

# def get_average(input_size: int, number_of_tests: int):
#     numbers_of_hires = []
#     for _ in range(number_of_tests):
#         numbers_of_hires.append(test_input_size(input_size))
#     return sum(numbers_of_hires) / len(numbers_of_hires)