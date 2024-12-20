import numpy as np
def gradient_descent(func, gradfunc, startpoint, learningrate=0.001, maxiters=9999, tolerance=1e-6):
    point = np.array(startpoint)
    for i in range(maxiters):
        gradient = np.array(gradfunc(point)) 
        next_point = point - learningrate * gradient  
        # если градиента мало, останавливается
        if np.linalg.norm(gradient) < tolerance:
            print(f"вышло за {i+1} итераций.")
            break
        
        point = next_point  # Обновляем  (как в ноудлист)
    
    return point, func(point)
# я использовал толеранс цифру которую нашел в интернете, если есть ошибки то попрошу сообщить спасибо