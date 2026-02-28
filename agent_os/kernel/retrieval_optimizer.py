class RetrievalOptimizer:
    def __init__(self):
        self.strategy_weight = 1.0

    def optimize(self, user_feedback_score):
        if user_feedback_score < 0.5:
            self.strategy_weight -= 0.1
        else:
            self.strategy_weight += 0.1
            
        self.strategy_weight = max(0.1, min(self.strategy_weight, 2.0))
        return self.strategy_weight