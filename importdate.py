from datetime import datetime, timedelta
i = 1181
while i<=1200:
    prev_date = (datetime.now() - timedelta(i)).strftime('%Y-%m-%d')
    print (i)
    print (prev_date)
    i+=1
