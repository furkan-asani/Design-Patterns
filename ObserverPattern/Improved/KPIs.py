from AbsSubject import AbsSubject

class KPIs(AbsSubject):
    _openTickets = -1
    _closedTickets = -1
    _newTickets = -1

    @property
    def openTickets(self):
        return self._openTickets

    @property
    def closedTickets(self):
        return self._closedTickets

    @property
    def newTickets(self):
        return self._newTickets

    def setKPIs(self, openTickets, closedTickets, newTickets):
        self._openTickets = openTickets
        self._closedTickets = closedTickets
        self._newTickets = newTickets
        self.notify()
