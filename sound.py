import board
import time
import pulseio
buzzer = pulseio.PWMOut(board.D5, variable_frequency=True)
buzzer.frequency = 440
OFF = 0
ON = 2**15
buzzer.duty_cycle = ON
time.sleep(1)
buzzer.duty_cycle = OFF
