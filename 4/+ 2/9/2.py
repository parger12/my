import numpy as np
adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var)
adv_time = adv_mean + 3 * adv_std
print(f"Время показа сообщения {adv_time} секунд.")
