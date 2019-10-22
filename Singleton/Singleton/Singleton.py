class Singleton:
    __singleton = None

    def __new__(cls):
        if cls.__singleton is None:
            cls.__singleton = super().__new__(cls)
            print('THe instance is created')
        return cls.__singleton
