from typing import Any


class HashMap:
    def __init__(self):
        self.size = 8
        self.map = [None] * self.size

    def _get_hash(self, key) -> int:
        return hash(key) % self.size

    def add(self, key, value) -> None:
        """Добавляет пару ключ-значение в хеш-таблицу"""

        # получаем хэш ключа
        key_hash = self._get_hash(key)

        # Если ячейка пуста, то добавляем хэш и ключ-значение
        if self.map[key_hash] is None:
            self.map[key_hash] = (key_hash, key, value)
        else:
            # Иначе ищем свободную ячейку для добавления пары ключ-значение
            new_hash = self._probe(key_hash)
            # Если нашли свободную ячейку, то добавляем пару ключ-значение
            if new_hash is not None:
                self.map[new_hash] = (key_hash, key, value)
            else:
                # Иначе увеличиваем размер хещ=таблицы и повторно добавляем пару ключ-значение
                self._resize()
                self.add(key, value)

    def _probe(self, start_index) -> int | None:
        """Ищем свободную ячейку для добавления пары ключ-значение."""
        # Проходим по всем ячейкам хеш-таблицы
        for i in range(start_index + 1, self.size + start_index):
            index = i % self.size
            # Если ячейка пуста, то возвращаем индекс ячейки
            if self.map[index] is None:
                return index

    def _resize(self) -> None:
        """
        Увеличиваем размер хеш-таблицы в два раза и перенеосит все элементы в новую.
        Важно! что тут может пересчитаться индекс элемента.
        :return:
        """
        old_map = self.map
        self.size *= 2
        self.map = [None] * self.size
        for item in old_map:
            if item is not None:
                _, key, value = item
                self.add(key, value)

    def get(self, key) -> Any | None:
        """Возвращает значение по ключу."""
        # Получаем хеш ключа
        key_hash = self._get_hash(key)
        # Если ячейка не пуста и ключ совпадает, то возвращаем значение
        if self.map[key_hash] is not None and self.map[key_hash][1] == key:
            return self.map[key_hash][2]
        else:
            # Иначе ищем значение по ключу
            for i in range(key_hash + 1, self.size + key_hash):
                index = i % self.size
                if self.map[index] is not None and self.map[index][1] == key:
                    return self.map[key_hash][2]
        return None

    def delete(self, key) -> bool:
        """Удаляет значение по ключу."""
        # Получаем хеш ключа
        key_hash = self._get_hash(key)
        # Если ячейка не пуста и ключ совпадает, то возвращаем значение
        if self.map[key_hash] is not None and self.map[key_hash][0] == key:
            self.map[key_hash] = None
            return True
        else:
            # Иначе ищем значение по ключу
            for i in range(key_hash + 1, self.size + key_hash):
                index = i % self.size
                if self.map[index] is not None and self.map[index][0] == key:
                    self.map[key_hash] = None
                    return True
        return False

    def __str__(self):
        result = ""
        for item in self.map:
            if item is not None:
                result += str(item) + "\n"
        return result


hash_map = HashMap()
hash_map.add("key1", "value1")
hash_map.add("key2", "value2")
hash_map.add("key3", "value3")

print(hash_map)