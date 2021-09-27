from KPIs import KPIs
from CurrentKPIs import CurrentKPIs
from ForecastKPIs import ForecastKPIs

# Report on current KPI values
with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.setKPIs(25, 10, 5)
        kpis.setKPIs(100, 50, 30)
        kpis.setKPIs(33, 12, 99)
        
print('\n*** Exited the context managers. ***\n\n')
kpis.setKPIs(42, 69, 3)