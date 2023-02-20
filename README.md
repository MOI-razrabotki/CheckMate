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
1. **Настя** занималась оформлением и представлением всех результатов командной работы.
2. **Кирилл** подбирал необходимые материалы и комплектующие, он был ответственен за монтаж электротехнической схемы и сборку всего устройства. Также был оператором и монтажером видеоматериалов.
3. **Вадим** работал с микрокомпьютером Raspberry Pi. Он разрабатывал программное обеспечение для всей системы, выстраивал алгоритмы искусственного интеллекта, распознавания речи, передвижения фигур.
4. **Андрей** визуализировал в системе автоматизированного проектирования трехмерные модели совместно разработанного прототипа, его составных частей.

## Видео разработанного продукта
* Командное видео с разработанным продуктом [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://youtu.be/5s41Iof64gM)
    [![Просмотр видео](./img/video_previews/video_preview_1.jpg)](https://youtu.be/5s41Iof64gM)
* Видео с полной демонстрацией функционирования продукта [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://youtu.be/BVJHFvGekIg)
    [![Просмотр видео](./img/video_previews/video_preview_2.png)](https://youtu.be/BVJHFvGekIg)

# Кратко о функционале

<p align="center">
<img src="./img/slides/hardware_slide.png" alt="Слайд функционала" width="800">
</p>

<p align="center">
<img src="./img/slides/user_guide.png" alt="Краткое руководство" width="800">
</p>

## Фотографии

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

## 3d-модели

**⚠️ Чтобы наши 3d-модели не украли, мы не стали выкладывать файлы с ними в открытый доступ. Они загружены на специальный онлайн-сервис, где вы можете ознакомиться с каждым компонентом системы.**

* 3d-модель Core-XY конструкции кареток [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://a360.co/3Shld8j)
    [![Просмотр модели](./img/render_previews/peview_render_1.png)](https://a360.co/3Shld8j)
* 3d-модель ЧекМейта [![](https://img.shields.io/badge/*%20%D1%82%D1%8B%D0%BA%20*-lightgrey)](https://skfb.ly/oEpMO)
    [![Просмотр модели](./img/render_previews/preview_render_2.png)](https://skfb.ly/oEpMO)

## 3d-рендеры

<p align="center">
<img src="./img/renders/render_CheckMate_1.png" alt="3d рендер продукта" width="800">
</p>
<p align="center">
<img src="./img/renders/render_CheckMate_2.png" alt="3d рендер продукта" width="800">
</p>
<p align="center">
<img src="./img/renders/render_CheckMate_3.png" alt="3d рендер продукта" width="800">
</p>

## Функциональное описание в виде UML-Диаграмм

* Use Case Diagram (диаграмма прецедентов)
    <p align="center">
    <img src="./img/diagrams/Use_Case_Diagram_CM.png" alt="Use Case Diagram" width="800" style="background-color:white;">
    </p>
* State Machine Diagram (диаграмма состояний)
    <p align="center">
    <img src="./img/diagrams/State_Machine_Diagram_CM.png" alt="State Machine Diagram" width="800" style="background-color:white;">
    </p>
* Sequence Diagram (диаграмма последовательности)
    <p align="center">
    <img src="./img/diagrams/Sequence_Diagram_CM.png" alt="Sequence Diagram" width="800" style="background-color:white;">
    </p>
* Component Diagram (диаграмма компонентов)
    <p align="center">
    <img src="./img/diagrams/Component_Diagram_CM.png" alt="Component Diagram" width="800" style="background-color:white;">
    </p>

## Исходный код

**⚠️ Мы отказались от полной публикации исходного кода в репозитории. Вместо этого была размещена только его малая часть. Это сделано для того, чтобы обезопасить себя от любителей воровать чужой код, ибо исходники являются коммерческой тайной.**

Часть кода распололожена в каталоге [```src```](https://github.com/MOI-razrabotki/CheckMate/tree/main/src)
