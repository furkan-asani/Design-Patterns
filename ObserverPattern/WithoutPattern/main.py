from kpi_data import KPI_Data

# Report on current KPI values
for kpi in KPI_Data:
    if kpi.name == 'open':
        print('Current open tickets: %s' % kpi.value)
    elif kpi.name == 'new':
        print('New tickets in the last hour: %s' % kpi.value)
    elif kpi.name == 'closed':
        print('Closed tickets in the last hour: %s' % kpi.value)

# Problem is the extensibility 
# what if the values should also be sent to your boss via this application
# and also to another REST-API? What if there are new KPIs? 
# This gets cumbersome very quickly
# Luckily there is a better way to decouple the subject and observer