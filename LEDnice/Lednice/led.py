from gpiozero import PWMLED

ledR= PWMLED(16)
ledG = PWMLED(20)
ledB = PWMLED(21)

# 0 > 0
# 1 > 255

ledR.value = 1  # off
ledG.value = 0.1  # off
ledB.value = 0.5  # off