import time
import math

def sqrt_after_delay(number, delay_ms):
    delay_seconds = delay_ms/1000 # Преобразовать миллисекунды в секунды
    time.sleep(delay_seconds) # Дождитесь указанной задержки
    result = math.sqrt(number) # Вычислить квадратный корень
    return result
number = 25100
delay_ms = 2123

result = sqrt_after_delay(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {result}")