def score_evaluation(scores):
    
    for i in scores:
        if i < 50:
            print("Fail")
            continue
            
        else:
            print("Pass")
        
    
    

scores = [72, 45, 89, 30, 60]
score_evaluation(scores)