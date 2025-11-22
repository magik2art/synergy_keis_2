# ------------------------------
# Кейс-задача №2
# Демонстрация работы методов базового и производного классов.
#
# Базовый класс: Employee (сотрудник)
# Производный класс: Manager (руководитель)
# ------------------------------


class Employee:
    """Базовый класс, описывающий сотрудника."""

    def __init__(self, name: str, base_salary: float) -> None:
        # Имя сотрудника
        self.name = name
        # Базовый оклад
        self.base_salary = base_salary

    def get_info(self) -> str:
        """Вернуть текстовое описание сотрудника."""
        return f"Сотрудник: {self.name}, оклад: {self.base_salary} руб."

    def calculate_salary(self) -> float:
        """
        Рассчитать зарплату.
        Для обычного сотрудника — просто базовый оклад.
        Метод потом будет переопределён в производном классе.
        """
        return self.base_salary


class Manager(Employee):
    """Производный класс, описывающий руководителя."""

    def __init__(self, name: str, base_salary: float, bonus: float) -> None:
        # Вызываем конструктор базового класса
        super().__init__(name, base_salary)
        # Дополнительное поле: бонус руководителя
        self.bonus = bonus

    def get_info(self) -> str:
        """
        Переопределяем метод get_info().
        Дополняем информацию из базового класса данными о бонусе.
        """
        base_info = super().get_info()
        return f"{base_info} (руководитель, бонус: {self.bonus} руб.)"

    def calculate_salary(self) -> float:
        """
        Переопределяем расчёт зарплаты.
        Для руководителя: оклад + бонус.
        """
        # Можно использовать super().calculate_salary(), чтобы не дублировать логику
        return super().calculate_salary() + self.bonus


if __name__ == "__main__":
    print("=== Демонстрация работы базового и производного классов ===\n")

    # Создаём объект базового класса
    emp = Employee(name="Иван Петров", base_salary=70_000)
    # Создаём объект производного класса
    mgr = Manager(name="Павел Смирнов", base_salary=90_000, bonus=50_000)

    print("--- Базовый класс Employee ---")
    print(emp.get_info())
    print("Расчёт зарплаты сотрудника:", emp.calculate_salary(), "руб.\n")

    print("--- Производный класс Manager ---")
    print(mgr.get_info())
    print("Расчёт зарплаты руководителя:", mgr.calculate_salary(), "руб.\n")

    print("--- Полиморфизм в действии ---")
    employees = [emp, mgr]  # список с объектами разных классов

    for e in employees:
        # Здесь у каждого объекта вызывается СВОЯ версия calculate_salary()
        print(f"{e.name}: зарплата = {e.calculate_salary()} руб.")
