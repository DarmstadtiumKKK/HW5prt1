import os
from collections import MutableMapping


class DirDict(MutableMapping):
    def __init__(self, way):
        self._way = way+'/'
        self._create_dir()

    def _create_dir(self):
        try:
            os.mkdir(self._way)
        except OSError:
            pass

    def _get_last_key(self):
        for file in os.listdir(self._way):
            pass
        return file

    def __setitem__(self, key, value):
        # Key - Имя файла
        # Value - Содержимое файла
        value=str(value)
        if type(key)!=str:
            key=str(key)
        file_path = self._way + key
        if os.access(file_path, os.F_OK) is False:
            print('создан файл '+key+' в словаре '+self._way[:len(self._way)-1])
        else:
            print('открыт файл '+key+' в словаре '+self._way[:len(self._way)-1])
        print('в файл '+key+' записано '+value+'\n')
        element = open(file_path, 'w')
        element.write(value + '\n')
        element.close()

    def __getitem__(self, item):
        # Item - имя файла
        # return содержимое файла
        file_path = self._way+item
        if os.access(file_path, os.F_OK) is False:
            raise KeyError
        element = open(file_path, 'r')
        value=element.read()
        element.close()
        return value[:len(value)-1]

    def __len__(self):
        return len(os.listdir(self._way))

    def __iter__(self):
        return iter(self)

    def __delitem__(self, key):
        print('Файл '+key+' из словаря '+self._way[:len(self._way)-1]+' удален'+'\n')
        os.remove(self._way+key)

    def __copy__(self, dat_way):
        new_dict=DirDict(dat_way)
        for file in os.listdir(self._way):
            with open(self._way+file) as element:
                new_dict[file] = element.read()
        return new_dict

    def values(self):
        for file in os.listdir(self._way):
            with open(self._way+file) as element:
                yield element.read().replace('\n','')

    def keys(self):
        for file in os.listdir(self._way):
            yield file

    def items(self):
        for file in os.listdir(self._way):
            with open(self._way+file) as element:
                yield (file, element.read().replace('\n',''))

    def clear(self):
        for file in os.listdir(self._way):
            self.__delitem__(file)

    def copy(self,path):
        return self.__copy__(path)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return None

    def pop(self, key, default='KeyErroR'):
        if key not in self.keys():
            if default=='KeyErroR':
                raise KeyError
            else:
                return default
        self.__delitem__(key)

    def popitem(self):
        if os.listdir(self._way) is []:
            raise KeyError
        key = self._get_last_key()
        with open(self._way + key) as element:
            item=(key,element.read().replace('\n',''))
        self.pop(key)
        return item

    def setdefault(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            self[key]=default

    def update(self, dict_with_new_data):
        for file in os.listdir(dict_with_new_data._way):
            if self.get(file) is None:
                path=dict_with_new_data._way
            else:
                path=self._way
            with open(path + file) as element:
                self[file]=element.read().replace('\n','')


MyDir=DirDict('dict_vault')
MyDir['key']=1  # Проверка setitem
MyDir['key1']='yes'
MyDir['key2']='2d6'
MyDir['key3']='lol'
MyDir['key4']='secret'
MyDir['key5']=34
print(MyDir['key'])  # Проверка getitem
print(list(MyDir.values()))  # Проверка Values
print(list(MyDir.keys())) # Проверка Keys
print(list(MyDir.items()))  # Проверка Items
Copy_dir=MyDir.copy('copy_vault')  # Проверка Copy
MyDir.clear()  # Проверка Clear
print(list(MyDir.items()))
print(MyDir.pop('key4',1))  # Проверка Pop
print(Copy_dir.popitem())  # Проверка Popitem
MyDir.setdefault('key3')  # Проверка Setdefault
print(list(MyDir.items()))
MyDir.clear()
MyDir.update(Copy_dir)  # Проверка Update
print(list(Copy_dir.items()))
print(list(MyDir.items()))






