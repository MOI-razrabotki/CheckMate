# CheckMate [![](https://img.shields.io/badge/CheckMate-blue?style=for-the-badge)](https://github.com/MOI-razrabotki/CheckMate)
> Шахматная доска с голосовым управлением и автоматизацией перемещения фигур

<img src="./img/MOI_razrabotki_logo.png" align="right" alt="Логотип команды МОИ разработки" width="100" />

**CheckMate** ```(ЧекМейт)``` - это автоматизированные роботизированные шахматы с голосовым управлением. Игра идет против искусственного интеллекта, устройство воспринимает голосовые команды человека, а система перемещения выставляет фигуру на заданную позицию. Предмет автоматизации заключается в том, что человек не должен касаться игрового поля или фигур во время шахматной партии.

Работа над проектным решением велась с учетом следующих ограничений:
* Разметка поля и схема расположения шахматных фигур соответствуют классическим шахматам.
* Отработанные фигуры должны парковаться в отдельные поля для белых и черных фигур.
* Сторона квадрата клетки игрового поля должна удовлетворять условию: ```a < 1,8d```, где ```d``` — диаметр подошвы фигуры
* Габариты устройства не превышают размеров ```800х800х800мм```.
* Конструкция шахмат вместе с системой перемещения должна размещаться в едином корпусе и быть устойчивой в процессе перемещения.

<p align="center">
  <img src="./img/CheckMate_box.png" alt="Коробка продукта CheckMate" width="700">
</p>

## Состав команды «МОИ разработки»
1. **Настя** - оформление и представление всего результата командной работы, презентацию проекта. 
1. **Кирилл** - подбор необходимых материалов и комплектующих, был ответственен за монтаж электротехнической схемы и сборку всего устройства. Также был оператором и монтажером видеоматериалов.
2. **Вадим**  - работа с программированием микрокомпьютера Raspberry Pi, разработка и внедрение алгоритмов искусственного интеллекта, распознавания речи, передвижения фигур и всей системы в целом.
3. **Андрей** - визуализирование в системе автоматизированного проектирования трехмерной модели совместно разработанному прототипу, его составных частей. 

## Видео разработанного продукта
* Командное видео с разработанным продуктом [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://youtu.be/5s41Iof64gM)
    [![Просмотр видео](./img/video_previews/video_preview_1.jpg)](https://youtu.be/5s41Iof64gM)
* Видео с полным функционированием продукта [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://youtu.be/UHgrxMTI6Ug)
    [![Просмотр видео](./img/video_previews/video_preview_2.png)](https://youtu.be/UHgrxMTI6Ug)

## Фотографии разработанного продукта

<p align="center">
<img src="./img/photos/14.jpg" alt="Фотография разработанного продукта" width="800">
</p>
<p align="center">
<img src="./img/photos/13.jpg" alt="Фотография разработанного продукта" width="800">
</p>
<p align="center">
<img src="./img/photos/10.jpg" alt="Фотография разработанного продукта" width="800">
</p>
<p align="center">
<img src="./img/photos/11.jpg" alt="Фотография разработанного продукта" width="800">
</p>
<p align="center">
<img src="./img/photos/4.jpg" alt="Фотография разработанного продукта" width="800">
</p>

## 3d-модели разработанного продукта

**⚠️ По причине опасения кражи наших 3d моделей было решено отказаться от прикрепления 3d моделей в виде файлов в тело нашего репозитория. Вместо этого было решено загрузить их на онлайн-сервис по просмотру 3d моделей.**

* 3d-модель Core-XY конструкции кареток [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://a360.co/3Shld8j)
    [![Просмотр модели](./img/render_previews/peview_render_1.png)](https://a360.co/3Shld8j)
* 3d-модель ЧекМейта с измененными полями [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://skfb.ly/oEpMO)
    [![Просмотр модели](./img/render_previews/preview_render_2.png)](https://skfb.ly/oEpMO)

## 3d-рендеры разработанного продукта

<p align="center">
<img src="./img/renders/checkmate_1.png" alt="3d рендер продукта" width="800">
</p>
<p align="center">
<img src="./img/renders/checkmate_2.png" alt="3d рендер продукта" width="800">
</p>
<p align="center">
<img src="./img/renders/checkmate_3.png" alt="3d рендер продукта" width="800">
</p>

## Электротехническая схема разработанного устройства

<p align="center">
<img src="./img/circuit.jpg" alt="Электрическая схема" width="800">
</p>

## Функциональное описание в виде UML-Диаграмм

* Use Case Diagram
    <p align="center">
    <img src="./img/diagrams/CM_Use_Case_Diagram.png" alt="Use Case Diagram" width="800" style="background-color:white;">
    </p>
* State Machine Diagram
    <p align="center">
    <img src="./img/diagrams/CM_State_Machine_Diagram.png" alt="State Machine Diagram" width="800" style="background-color:white;">
    </p>
* Sequence Diagram
    <p align="center">
    <img src="./img/diagrams/CM_Sequence_Diagram.png" alt="Sequence Diagram" width="800" style="background-color:white;">
    </p>
* Component Diagram
    <p align="center">
    <img src="./img/diagrams/CM_Component_Diagram.png" alt="Component Diagram" width="800" style="background-color:white;">
    </p>

## Код продукта

**⚠️ По причине опасения кражи исходного кода было решено отказаться от его полной публикации в репозитории. Вместо этого была размещена только его малая часть.**

Часть кода распололожена в каталоге [```src```](https://github.com/MOI-razrabotki/CheckMate/tree/main/src)
