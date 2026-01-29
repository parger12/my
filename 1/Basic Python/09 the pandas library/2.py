import pandas as pd

music = [
        ['Bob Dylan', 'Like A Rolling Stone'],
        ['John Lennon', 'Imagine'],
        ['The Beatles', 'Hey Jude'],
        ['Nirvana', 'Smells Like Teen Spirit']
    ]

entries = ['artist', 'track']

playlist = pd.DataFrame(data=music, columns=entries)

print (playlist)