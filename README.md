
# 📊 Проект: Репликация из MySQL в ClickHouse через Debezium + Kafka + PySpark

## Цель
Организовать потоковую репликацию из MySQL в ClickHouse для построения аналитических витрин через Kafka, Debezium и PySpark. Репликация будет автоматизирована через Jenkins и в перспективе масштабируется в Google Cloud.

## Технологии
- MySQL
- Kafka
- Debezium
- PySpark
- ClickHouse
- Jenkins


## Состав проекта

- `docker-compose.yml` — запуск Kafka, Zookeeper, Connect и MySQL
- `etl/kafka_to_clickhouse.py` — парсинг CDC событий и запись в ClickHouse
- `jenkins/Jenkinsfile` — CI/CD пайплайн
- `sql/init_mysql.sql` — тестовая схема и данные
- `sql/clickhouse_views.sql` — витрины ClickHouse

## Проблемы и решения

- Kafka требовалась настройка `advertised.listeners`
- Debezium настройки `log_bin`, привилегии `REPLICATION SLAVE`
- ClickHouse типы, дублирование — решено нормализацией и фильтрацией
