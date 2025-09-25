users = {
    1: {"name": "Администратор", "role": "admin"},
    2: {"name": "Модератор", "role": "moderator"},
    3: {"name": "Обычный пользователь", "role": "user"},
    4: {"name": "Гость", "role": "guest"}
}

# Текущий пользователь
current_user = None


# Декоратор для проверки прав админ
def require_admin(func):
    def wrapper(user_id):
        global current_user

        # Проверяем, авторизован ли пользователь
        if current_user is None:
            print("❌ Ошибка: Пользователь не авторизован")
            return False

        # Проверяем, является ли пользователь администратором
        if current_user["role"] != "admin":
            print(f"❌ Ошибка: Доступ запрещен. Пользователь {current_user['name']} не является администратором")
            return False

        # Если проверка пройдена, вызываем функцию
        print(f"✅ Доступ разрешен для администратора {current_user['name']}")
        return func(user_id)

    return wrapper


# Функция удаления пользователя (только для админ)
@require_admin
def delete_user(user_id):
    """Удаляем пользователя из системы"""
    if user_id in users:
        deleted_user = users.pop(user_id)
        print(f"👤 Пользователь {deleted_user['name']} (ID: {user_id}) успешно удален")
        return True
    else:
        print(f"⚠️ Пользователь с ID {user_id} не найден")
        return False


# Доп функции
def login(user_id):
    """Входим в систему под указанным пользователем"""
    global current_user
    if user_id in users:
        current_user = users[user_id]
        print(f"🔑 Вход выполнен: {current_user['name']} (роль: {current_user['role']})")
        return True
    else:
        print("❌ Пользователь не найден")
        return False


def logout():
    """Выходим из системы"""
    global current_user
    if current_user:
        print(f"🚪 Выход выполнен: {current_user['name']}")
        current_user = None
    else:
        print("ℹ️ Нет активного пользователя")


def show_users():
    """Показываем всех пользователей"""
    print("\n📋 Список пользователей:")
    for user_id, user_info in users.items():
        print(f"ID: {user_id}, Имя: {user_info['name']}, Роль: {user_info['role']}")


# Демонстрация работы системы
def demo_access_control():
    print("--- Система проверки доступа ---\n")

    # Начальное состояние
    show_users()

    print("\n" + "-" * 50)

    # Тест 1: Попытка удаления без авторизации
    print("\n1. Попытка удаления без авторизации:")
    delete_user(3)  # Должно быть запрещено

    print("\n" + "-" * 50)

    # Тест 2: Обычный пользователь пытается удалить
    print("\n2. Обычный пользователь пытается удалить:")
    login(3)  # Вход как обычный пользователь
    delete_user(2)  # Должно быть запрещено

    print("\n" + "-" * 50)

    # Тест 3: Модератор пытается удалить
    print("\n3. Модератор пытается удалить:")
    login(2)  # Вход как модератор
    delete_user(3)  # Должно быть запрещено

    print("\n" + "-" * 50)

    # Тест 4: Администратор успешно удаляет
    print("\n4. Администратор успешно удаляет:")
    login(1)  # Вход как администратор
    delete_user(3)  # Должно быть разрешено

    print("\n" + "-" * 50)

    # Тест 5: Попытка удаления несуществующего пользователя
    print("\n5. Попытка удаления несуществующего пользователя:")
    delete_user(999)  # Пользователь не найден

    print("\n" + "-" * 50)

    # Показываем конечное состояние
    print("\nФинальное состояние базы пользователей:")
    show_users()

    # Выход из системы
    logout()


if __name__ == "__main__":
    demo_access_control()

