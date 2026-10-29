#algorithm from CLRS 4th edition page 115
def hire_assistant(candidates: list[int]):    
    if len(candidates) == 0:
        print("No candidates to choose from. Terminating...")
        return 0
    
    best = candidates[0]
    total_hires = 1

    for i in range(1, len(candidates)):
        if candidates[i] > best:
            best = candidates[i]
            total_hires += 1

    return total_hires
