class PlayerRecords:

    @staticmethod
    def get_top_10():
        pass

    @staticmethod
    def get_top_100():
        pass

    @staticmethod
    def add_record(record):
        pass


# top_10 = PlayerRecords.get_top_10()


class Cat:
    def say(self):
        self.what_does_cat_say()

    @staticmethod
    def what_does_cat_say():
        print('Grhhhpp')


Cat.what_does_cat_say()
cat1 = Cat()
cat1.what_does_cat_say()
#
cat2 = Cat()
cat2.say()
