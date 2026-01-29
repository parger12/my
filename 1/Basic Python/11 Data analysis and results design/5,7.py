import pandas as pd
df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\music_log_upd.csv')
genre_grouping = df.groupby('user_id')['genre_name']
genre_counting = genre_grouping.count()
print(genre_counting.head(15))

def user_genres(group):
    for user_id, values in group:
        if len(values)>50:
            return user_id
        

search_id = user_genres(genre_grouping)
print(search_id)

music_user = df[df['user_id'] == search_id]
music_user = music_user[music_user['total_play_seconds'] != 0]

sum_music_user = music_user.groupby('genre_name')['total_play_seconds'].sum()

print(sum_music_user)

count_music_user = music_user.groupby('genre_name')['genre_name'].count()
print(count_music_user)

final_sum = sum_music_user.sort_values(ascending=False)
#print(final_sum)

final_count = count_music_user.sort_values(ascending=False)

print (final_count)