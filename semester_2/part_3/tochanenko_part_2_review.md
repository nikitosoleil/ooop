### 1. Наскільки моделі є зрозумілими, наскільки вони описують предметну область, структуру та поведінку відповідної системи?
Моделі є зрозумілими, але їх кількості недостатньо для повного описання структури та поведінки системи.

### 2. Чи є якісь аспекти, які видаються важливими, але не відображені в моделі (на діаграмах)?
Присутня лише діаграма класів - багато аспектів залишено не відображеними.	

### 3. Чи є в моделі щось зайве, якісь аспекти описані занадто детально?
Описання моделі є в міру детальним.

### 4. Наскільки доцільно використані різні типи діаграм?
Єдина діаграма (класів) використана доцільно.

### 5. Наскільки коректно використана нотація UML, різні елементи та конектори?
Повністю коректно.

### 6. Наскільки вдалим є глосарій? Чи всі важливі поняття предметної області описано? Чи немає неоднозначностей?
Глосарій відсутній.

### 7. Чи всі важливі сценарії використання описано в моделі? Наскільки зрозумілі різні сценарії, зв’язки між ними?
Сценарії відсутні.

### 8. Наскільки доцільним є поділ системи на частини/компоненти/модулі/...?
Поділ відсутній.

### 9. Наскільки доцільними є зв’язки між компонентами/класами/об’єктами? Чи немає занадто тісно зв’язаних компонентів?
Зв'язки між класами доцільні.

### 10. Наскільки object-oriented design відповідає загальним принципам?
Для реалізації двох методів зберігання графів - матрицею (GraphMatrix) та списками суміжності (GraphList) - використано наслідування від базового класу графа Graph. Це можна замінити композицією: один клас графу Graph, до якого входить об'єкт класу Storage, що відповідає за метод зберігання графу. Це більш відповідає загальним принципам.