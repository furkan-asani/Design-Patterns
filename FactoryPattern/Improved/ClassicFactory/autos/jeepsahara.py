from .abs_auto import AbsAuto


class JeepSahara(AbsAuto):
    def start(self):
        print("%s is roaring!" % self.name)

    def stop(self):
        print("%s goes to sleep." % self.name)
