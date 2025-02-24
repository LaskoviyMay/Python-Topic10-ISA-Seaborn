import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из JSON-файла
file_path = 'events.json'

# Чтение JSON-файла
with open(file_path, 'r', encoding='utf-8') as file:
    data = pd.read_json(file)

# Преобразование данных в датафрейм
df = pd.json_normalize(data['events'])

# Создание новой колонки "category" для группировки событий
def categorize_signature(signature):
    if 'MALWARE' in signature:
        return 'Malware'
    elif 'EXPLOIT' in signature:
        return 'Exploit'
    elif 'INDICATOR' in signature:
        return 'Indicator'
    elif 'NETBIOS' in signature:
        return 'Network'
    else:
        return 'Other'

# Применение функции для создания новой колонки
df['category'] = df['signature'].apply(categorize_signature)

# Подсчет количества событий в каждой категории
category_counts = df['category'].value_counts().reset_index()
category_counts.columns = ['category', 'count']

# Визуализация с использованием Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=category_counts, x='category', y='count', palette='viridis')
plt.title('Распределение типов событий информационной безопасности', fontsize=16)
plt.xlabel('Категория события', fontsize=12)
plt.ylabel('Количество событий', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()