# Реализовать сервис, который принимает и отвечает на HTTP запросы.

## Функционал:
1.В случае успешной обработки сервис должен
отвечать статусом 200, в случае любой ошибки —
статус 400.

2.Сохранение всех объектов в базе данных.

3.Запросы

GET /city/ — получение всех городов из базы;
GET /city//street/ — получение всех улиц города;
(city_id — идентификатор города)
POST /shop/ — создание магазина; Данный метод
получает json c объектом магазина, в ответ
возвращает id созданной записи.
GET /shop/?street=&city=&open=0/1
{ — получение
списка магазинов;
Метод принимает параметры для фильтрации.
Параметры не обязательны. В случае отсутствия
параметров выводтся все магазины, если хоть
один параметр есть , то по нему выполнется
фильтрация.
Важно!: в объекте каждого магазина
выводится название города и улицы, а не id
записей.

Параметр open: 0 - закрыт, 1 - открыт. Данный
статус определется исход из параметров
<Время открытия>, ¢Время закрытия» и текущего
времени сервера.

## Объекты:.
Магазин:
Название ̧
Город
Улица
Дом
Время открытия
Время закрытия

Город:
Название

Улица:
Название
Город

!! Замечание: поле id у объектов не указаны, но
подразумевается что они есть
!! Важно: Выстроить связи между таблицами в базе
данных.

## Инструменты:

Фреймворк для обработки http запросов Django +
Django Rest Framework

РеляциоNNая БД (PostgreSQL - предпочтительно,
MySQL и тд)
Запросы в базу данных через ORM (ORM Nа выбор).
