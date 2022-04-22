adj = ['amazing', 'cool', 'nice', 'angry', 'sad', 'mad']

names = ['Ashvin', 'Akash', 'Elango', 'Gita']

size = len(adj)



for adjective in adj:
    for name in names:
        if (adjective == 'sad') and (name == 'Elango'):
            continue
        print(adjective + " "+ name)
    
