class UrTube:
    """
    Класс UrTube, содержащий атрибуты: список объектов (User): список объектов (Video),
    текущий пользователь (User)
    """
    def __init__(self users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user
    def log_in(self, nickname, password):
        pass

    def register(self, nickname, password, age):
        pass

    def log_out(self):
        pass
    def add(self):
        pass
    def get_videos(self):
        pass
    def watch_video(self):
        pass
class Video:
    """
    Класс видео, содержащий атрибуты: заголовок (строка); продолжительность (секунды);
    секунда остановки (изначально 0); ограничение по возрасту (bool (False по умолчанию));
    """
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    """
    Класс пользователь, содержащий атрибуты: имя пользователя (строка);  password(в хэшированном виде, число);
    age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')