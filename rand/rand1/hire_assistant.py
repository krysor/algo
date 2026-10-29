#algorithm from CLRS 4th edition page 115
def hire_assistant(candidates: list[int]):    
    if len(candidates) == 0:
        print("No candidates to choose from... Terminating")
        return
    
    best = candidates[0]
    print(f"Hiring candidate {0}: {candidates[0]}")
    for i in range(1, len(candidates)):
        if candidates[i] > best:
            best = candidates[i]
            print(f"Hiring candidate {i}: {candidates[i]}") 
