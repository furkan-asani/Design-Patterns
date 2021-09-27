from AbsObserver import AbsObserver

class ForecastKPIs(AbsObserver):
    openTickets = -1
    closedTickets = -1
    newTickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.openTickets = self._kpis.openTickets
        self.closedTickets = self._kpis.closedTickets
        self.newTickets = self._kpis.newTickets
        self.display()

    def display(self):
        print('Forecast open tickets: {}'.format(self.openTickets+2))
        print('New tickets expected in the next hour: {}'.format(self.newTickets+6))
        print('Expected closed tickets in the next half hour: {}'.format(self.closedTickets-1))
        print('*****\n')