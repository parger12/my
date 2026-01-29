def find_rect_square(side1, side2):
    square = side1*side2
    return square

print (find_rect_square(10,12))




def is_speed_ok (speed, normal_speed=60):
    return speed <= normal_speed

current_speed = 46
print(is_speed_ok(current_speed))
current_speed = 70
print(is_speed_ok(current_speed))
current_speed = 60
print(is_speed_ok(current_speed))



def get_hours_and_minutes(time_string):
    hours, minutes = time_string.split (':')
    str_hours = int(hours)
    str_minutes = int(minutes)
    return str_hours, str_minutes

time_str = '12:35'
hours, minutes = get_hours_and_minutes(time_str)
print(hours, minutes)



def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s

def check_song_duration(time_string):
    minut, secund = get_minutes_and_seconds(time_string)
    secund_full = minut * 60 + secund
    return secund_full < 210

print(check_song_duration('4:35'))
print(check_song_duration('2:10'))




def get_minutes_and_seconds(time_string):
    time_list = time_string.split(':')
    m = int(time_list[0])
    s = int(time_list[1])
    return m, s
def check_song_duration(time_string):
    minutes, seconds = get_minutes_and_seconds(time_string)
    seconds = minutes * 60 + seconds
    return seconds <= 210
tracks = ['2:25', '2:35', '3:45', '2:00', '5:10']
for track in tracks:
    check_song = check_song_duration(track)
    print (check_song)
