import hashlib

class User:
    """
    Базовый класс пользователя.
    Хранит общие свойства и методы для всех пользователей.
    """
    users = []  # Статический список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        # Сохраняем хеш пароля (безопасное хранение)
        self.password = User.hash_password(password)
        # Добавляем пользователя в общий список
        User.users.append(self)

    @staticmethod
    def hash_password(password):
        """
        Статический метод для хеширования пароля.
        Использует алгоритм SHA-256.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Статический метод для проверки пароля.
        Сравнивает хеш сохраненного пароля с хешом введенного.
        """
        return stored_password == User.hash_password(provided_password)

    def get_details(self):
        """Возвращает основные детали пользователя."""
        return f"User: {self.username}, email: {self.email}"


class Customer(User):
    """
    Класс клиента. Наследуется от User.
    Добавляет свойство 'адрес'.
    """
    def __init__(self, username, email, password, address):
        # Вызываем конструктор родительского класса
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        """Переопределяем метод для вывода дополнительной информации."""
        return f"Customer: {self.username}, email: {self.email}, address: {self.address}"


class Admin(User):
    """
    Класс администратора. Наследуется от User.
    Добавляет свойство 'уровень доступа'.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        """Переопределяем метод для вывода дополнительной информации."""
        return f"Admin: {self.username}, email: {self.email}, admin_level: {self.admin_level}"

    @staticmethod
    def list_users():
        """Выводит список всех зарегистрированных пользователей."""
        if not User.users:
            print("No users registered.")
            return
        for user in User.users:
            print(user.get_details())

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени.
        Возвращает сообщение о результате операции.
        """
        for user in User.users:
            if user.username == username:
                User.users.remove(user)
                return f"User {username} deleted."
        return f"User {username} not found."