class Computer(object):
    def __init__(self, case, mainboard, cpu, memory, hardDrive, videoCard):
        self.case = case
        self.mainboard = mainboard
        self.cpu = cpu
        self.memory = memory
        self.hardDrive = hardDrive
        self.videoCard = videoCard
    
    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard Drive', self.hardDrive))
        print('\t{:>10}: {}'.format('Video Card', self.videoCard))
