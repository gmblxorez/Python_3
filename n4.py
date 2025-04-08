from typing import List, Dict, Optional


class MusicBand:
    """Класс, представляющий музыкальную группу"""

    # Атрибуты класса
    total_bands = 0
    music_genres = ["Rock", "Pop", "Jazz", "Hip-Hop", "Electronic"]

    def __init__(self, name: str, year_formed: int, members: List[str],
                 genre: str, albums: int = 0) -> None:
        """
        Инициализация музыкальной группы

        :param name: Название группы
        :param year_formed: Год основания
        :param members: Список участников
        :param genre: Музыкальный жанр
        :param albums: Количество выпущенных альбомов
        """
        self.name = name
        self.year_formed = year_formed
        self.members = members
        self.genre = genre
        self.albums = albums
        self.is_active = True

        MusicBand.total_bands += 1

    def __str__(self) -> str:
        """Строковое представление группы"""
        status = "активна" if self.is_active else "неактивна"
        return (f"Группа '{self.name}' ({self.genre}), основана в {self.year_formed}. "
                f"Состав: {', '.join(self.members)}. Статус: {status}")

    def add_member(self, new_member: str) -> None:
        """Добавляет нового участника в группу"""
        self.members.append(new_member)
        print(f"{new_member} присоединился к группе {self.name}")

    def release_album(self) -> None:
        """Увеличивает счетчик выпущенных альбомов"""
        self.albums += 1
        print(f"{self.name} выпустила новый альбом! Всего альбомов: {self.albums}")

    def disband(self) -> None:
        """Деактивирует группу"""
        self.is_active = False
        print(f"Группа {self.name} прекратила существование")

    def years_active(self, current_year: int) -> int:
        """Вычисляет сколько лет группа существует"""
        if current_year < self.year_formed:
            raise ValueError("Текущий год не может быть меньше года основания")
        return current_year - self.year_formed

    @classmethod
    def get_genre_info(cls) -> Dict[str, int]:
        """Возвращает информацию о жанрах в виде словаря"""
        return {genre: idx + 1 for idx, genre in enumerate(cls.music_genres)}


# Создаем объекты
beatles = MusicBand("The Beatles", 1960, ["John Lennon", "Paul McCartney",
                                          "George Harrison", "Ringo Starr"], "Rock", 12)

pink_floyd = MusicBand("Pink Floyd", 1965, ["Roger Waters", "David Gilmour",
                                            "Nick Mason", "Richard Wright"], "Progressive Rock", 15)

# Используем методы
print(beatles)
print(pink_floyd)

beatles.add_member("Billy Preston")
pink_floyd.release_album()

print(f"\nГруппа {beatles.name} существует {beatles.years_active(2025)} лет")
print(f"Всего групп создано: {MusicBand.total_bands}")
print(f"Доступные жанры: {MusicBand.music_genres}")

pink_floyd.disband()
print(pink_floyd)