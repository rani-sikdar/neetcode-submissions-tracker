class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        # x = float(init)
        
        # for _ in range(iterations):
        #     gradient = 2 * x
        #     x = x - learning_rate * gradient
        
        # x= round(x, 5)

        # # Convert to int if it's a whole number
        # if x.is_integer():
        #     return int(x)
        
        # return x

        if iterations == 0:
            return init
        
        x = float(init)
        
        for _ in range(iterations):
            x = x - learning_rate * (2 * x)
        
        return round(x, 5)
