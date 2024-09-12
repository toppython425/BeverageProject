from beverage import Soda, DietSoda

if __name__ == "__main__":
    """Добавлен интерфейс пользователя"""
    soda_1 = Soda("Coca Cola", 1.0, 90, "Вкус Колы")
    soda_2 = Soda("Pepsi", 1.5, 120, "Вкус Пепси")
    diet_soda_1 = DietSoda("Cola Zero", 1.0, 95, "Вкус Колы Диетической")
    diet_soda_2 = DietSoda("Diet Pepsi ", 1.5, 130, "Вкус Пепси Диетической")

    print(soda_1.describe(), end="\n\n")
    print(soda_2.describe(), end="\n\n")
    print(diet_soda_1.describe(), end="\n\n")
    print(diet_soda_2.describe(), end="\n\n")

