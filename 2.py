time_user = int(input("Введите время в секундах:"))
time_hour = int(time_user / 3600)
time_minute_cal = float((float(time_user / 3600) - time_hour) * 60)
time_minute_result = int(time_minute_cal)
time_second = (time_minute_cal - time_minute_result) * 60
print(f"{time_hour:02}:{time_minute_result:02}:{time_second:02.0f}")
