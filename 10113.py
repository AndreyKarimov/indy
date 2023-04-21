week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = ((i, week_days[(i + 4) % 7]) for i in range(1, 78))
print(*days, sep='\n')
