# Store warehouse

## Функционал для обработки информации по товару.

## Для использования:
  + клонируйте репозиторий: [GitHub](https://github.com/Kristina-Maximova/project-7)
  + установите зависимости: 

    1. python = "^3.13"
    

## Примеры использования

  В проекте используются классы:
  > *Product*   
  >>Smartphone
  > 
> >LawnGrass
  
> *Сategory*.

Реализована возможность складывать между собой товары одной категории.
Результатом будет суммарная стоимость складываемых товаров. 

Например:
```commandline
smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "Серый")
smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

smartphone_sum = smartphone1 + smartphone2

print(smartphone_sum)

>>> 2580000.0
```
 
 

