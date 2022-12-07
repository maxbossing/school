# **School**
scripts/Programms written for IT Class

---

> ### This is not exacty the code we used in the class
> ### I gave myself the task to always minimize the amount of lines of code needed

---

## **Index**
+ [mouse_population.py](https://github.com/maxbossing/school/blob/main/mouse_population.py)
    + Calculates the population of a mouse colony based on some basic factors
+ [germany_population.py](https://github.com/maxbossign/school/blob/main/germany_population.py)
    + Calculates the population of germany based on the population data of 2005
---

## **[mouse_population.py](https://github.com/maxbossing/school/blob/main/mouse_population.py)**
Calculates the population of a mouse colony based on some basic factors
> Iterates through defined "years", every iteration, the population changes on these factors:
> 1. Half of the young die, the rest gets old
> 2. 2 Thirds of the old die, the rest gets elderly
> 3. every old persoin gives birth to 4 young, every elderly to 2
> 4. All elderly die

## **[germany_population.py](https://github.com/maxbossing/school/blob/main/germany_population.py)**
Calculates the population of germany based on the population data of 2005
> Iterates through defined "years", every iteration, the population changes on these factors:
> #### **0-14**
> 1. 93% of people 0-14 stay in range 0-14
> 2. 6.6% of people 0-14 age 15-49
> 3. 0.4% of people 0-14 die  
> ---
> #### **15-49**
> 1. 2% of people in range 15-49 get kids(0-14)
> 2. 97% of peope aged 15-49 stay in range 15-49
> 3. 2.9% of people 15-49 age 50-64
> 4. 0.1% of people 15-49 die
> ---
> #### **50-64**
> 1. 92.5% of people in range 50-64 stay in range 50-64
> 2. 6.6% of people 50-64 age 65+
> 3. 0.9% of people aged 50-64 die
> ---
> #### **65+**
> 1. 97.2% of people aged 65+ stay in range 65+
> 2. 2.8% of people aged 65+ die
