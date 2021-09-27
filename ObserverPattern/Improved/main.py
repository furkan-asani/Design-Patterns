from KPIs import KPIs
from CurrentKPIs import CurrentKPIs
from ForecastKPIs import ForecastKPIs

# Report on current KPI values

kpis = KPIs()
CurrentKPIs = CurrentKPIs(kpis)
ForecastKPIs = ForecastKPIs(kpis)
kpis.setKPIs(25, 10, 5)
kpis.setKPIs(100, 50, 30)
kpis.setKPIs(33, 12, 99)

print('\n*** Detaching the currentKPIs observer. ***\n\n')
kpis.detach(CurrentKPIs)
kpis.setKPIs(42, 69, 3)