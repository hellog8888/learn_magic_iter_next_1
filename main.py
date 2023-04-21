class Person:
    def __init__(self, fio: str, job: str, old: (int, float), salary: (int, float), year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attrs = tuple(self.__dict__)
        self._len_attrs = len(self._attrs)
        self._iter_index = -1

    def __check_ind(self, ind):
        if type(ind) != int and not (0 <= ind <= 4):
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        self.__check_ind(key)
        setattr(self, self._attrs[key], value)

    def __getitem__(self, key):
        self.__check_ind(key)
        return getattr(self, self._attrs[key])

    def __iter__(self):
        self._iter_index = -1
        return self

    def __next__(self):
        if self._iter_index < self._len_attrs - 1:
            self._iter_index += 1
            return getattr(self, self._attrs[self._iter_index])
        raise StopIteration