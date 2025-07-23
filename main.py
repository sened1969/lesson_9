# ======================
# 1. Импорт необходимых классов
# ======================
from classes import User, Customer, Admin


# ======================
# 2. Класс AuthenticationService
#    (управление пользователями и сессиями)
# ======================
class AuthenticationService:
    """Сервис для регистрации, входа и управления сессиями пользователей."""

    def __init__(self):
        self.current_user = None  # Текущий авторизованный пользователь

    def register(self, user_class, username, email, password, *args):
        """Регистрация нового пользователя с проверкой уникальности."""
        if any(user.username == username for user in User.users):
            return "Ошибка: имя пользователя уже занято."
        
        new_user = user_class(username, email, password, *args)
        return f"Пользователь {username} успешно зарегистрирован."

    def login(self, username, password):
        """Аутентификация пользователя."""
        user = next((u for u in User.users if u.username == username), None)
        if not user:
            return "Ошибка: пользователь не найден."
        if not User.check_password(user.password, password):
            return "Ошибка: неверный пароль."
        
        self.current_user = user
        return f"Добро пожаловать, {username}!"

    def logout(self):
        """Завершение текущей сессии."""
        if not self.current_user:
            return "Ошибка: нет активной сессии."
        username = self.current_user.username
        self.current_user = None
        return f"Сессия пользователя {username} завершена."

    def get_current_user(self):
        """Информация о текущем пользователе."""
        if not self.current_user:
            return "Нет активного пользователя."
        return self.current_user.get_details()


# ======================
# 3. Пример использования
# ======================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ СИСТЕМЫ")
    print("="*50 + "\n")
    
    # Инициализация сервиса
    auth_service = AuthenticationService()

    # Регистрация пользователей
    print("\n--- 1. Регистрация ---")
    print(auth_service.register(Customer, "alice", "alice@example.com", "qwerty", "ул. Пушкина, 10"))
    print(auth_service.register(Admin, "admin", "admin@example.com", "admin123", "super"))

    # Вход в систему
    print("\n--- 2. Вход ---")
    print(auth_service.login("alice", "qwerty"))  # Успешный вход
    print("Текущий пользователь:", auth_service.get_current_user())

    # Выход
    print("\n--- 3. Выход ---")
    print(auth_service.logout())

    # Административные функции
    print("\n--- 4. Администрирование ---")
    print(auth_service.login("admin", "admin123"))  # Вход как админ
    
    if isinstance(auth_service.current_user, Admin):
        print("\n[Админ] Список пользователей:")
        Admin.list_users()
        
        print("\n[Админ] Удаление пользователя 'alice':")
        print(Admin.delete_user("alice"))
        
        print("\n[Админ] Обновленный список пользователей:")
        Admin.list_users()
    else:
        print("Доступ запрещен: требуются права администратора.")