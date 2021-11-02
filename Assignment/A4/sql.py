import re
import mysql.connector
from mysql.connector import Error
import json
from decimal import Decimal
from fastapi import FastAPI
app = FastAPI()

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='sqlzoo',
                                        user='root',
                                        password='Test@123',auth_plugin='mysql_native_password')
    @app.get("/basics")
    def AllBasics():
            api1 = basics()
            api1.add("Question 1",(read_item(1)))
            api1.add("Question 2",(read_item(2)))
            api1.add("Question 3",(read_item(3)))
            return json.dumps(api1,cls=DecimalEncoder)

    @app.get("/basics/{item_id}")
    def read_item(item_id: int):
        if item_id ==1:
            if connection.is_connected():
                basics1 = """SELECT population FROM world WHERE name = 'Germany'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Modify it to show the population of Germany"""))
                api1.add("sql",(basics1))
                for row in record:
                    api1.add("Results",({"population":row[0]}))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id == 2:
            if connection.is_connected():
                basics1 = """SELECT name, population FROM world
    WHERE name IN ('Sweden', 'Norway', 'Denmark')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                ids = []
                for row in record:
                    ids.append({"name":row[0],"population":row[1]})
                api1.add("question",("""Show the name and the population for 'Sweden', 'Norway' and 'Denmark'."""))
                api1.add("sql",(basics1))
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)  
        elif item_id == 3:
            if connection.is_connected():
                basics1 = """SELECT name, area
    FROM world
        WHERE area BETWEEN 200000 AND 250000"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                ids = []
                for row in record:
                    ids.append({"name":row[0],"area":row[1]})
                api1.add("question",("""Which countries are not too small and not too big? BETWEEN allows range checking (range specified is inclusive of    
                boundary values). The example below shows countries with an area of 250,000-300,000 sq. km. Modify it to show the country and the area for countries with an area between 200,000 and 250,000."""))
                api1.add("sql",(basics1))
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)            

    @app.get("/world")
    async def Allworld():
            api1 = basics()
            api1.add("Question 1",(read_worlditem(1)))
            api1.add("Question 2",(read_worlditem(2)))
            api1.add("Question 3",(read_worlditem(3)))
            api1.add("Question 4",(read_worlditem(4)))
            api1.add("Question 5",(read_worlditem(5)))
            api1.add("Question 6",(read_worlditem(6)))
            api1.add("Question 7",(read_worlditem(7)))
            api1.add("Question 8",(read_worlditem(8)))
            api1.add("Question 9",(read_worlditem(9)))
            api1.add("Question 10",(read_worlditem(10)))
            api1.add("Question 11",(read_worlditem(11)))
            api1.add("Question 12",(read_worlditem(12)))
            api1.add("Question 13",(read_worlditem(13)))
            return json.dumps(api1,cls=DecimalEncoder)

    @app.get("/world/{item_id}")
    def read_worlditem(item_id: int):
        if item_id ==1:
            if connection.is_connected():
                basics1 = """SELECT name, continent, population FROM world"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Observe the result of running this SQL command to show the name, continent and population of all countries."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"continent":row[1],"population":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==2:
            if connection.is_connected():
                basics1 = """SELECT name
    FROM world
    WHERE population>=200000000"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==3:
            if connection.is_connected():
                basics1 = """SELECT name, gdp/population
    FROM world
    WHERE population >= 200000000"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Give the name and the per capita GDP for those countries with a population of at least 200 million"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"gdp/population":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==4:
            if connection.is_connected():
                basics1 = """SELECT name, population/1000000
    FROM world
    WHERE continent = 'South America'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"population/1000000":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==5:
            if connection.is_connected():
                basics1 = """SELECT name, population FROM world WHERE name in ('France', 'Germany', 'Italy')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and population for France, Germany, Italy"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"population":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==6:
            if connection.is_connected():
                basics1 = """SELECT name
    FROM world
    WHERE name LIKE '%united%'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the countries which have a name that includes the word 'United'"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==7:
            if connection.is_connected():
                basics1 = """SELECT name, population, area
    FROM world
    WHERE area > 3000000 OR population > 250000000
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the countries that are big by area or big by population. Show name, population and area."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"population":row[0],"area":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==8:
            if connection.is_connected():
                basics1 = """SELECT name, population, area
    FROM world
    WHERE (area > 3000000 AND population < 250000000)
    OR (area < 3000000 and population > 250000000)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Exclusive OR (XOR). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.

    Australia has a big area but a small population, it should be included.
    Indonesia has a big population but a small area, it should be included.
    China has a big population and big area, it should be excluded.
    United Kingdom has a small population and a small area, it should be excluded."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"population":row[0],"area":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==9:
            if connection.is_connected():
                basics1 = """SELECT name, ROUND(population/1000000,2), ROUND(gdp/1000000000, 2)
    FROM world
    WHERE continent = 'South America'
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and population in millions and the GDP in billions for the countries of the continent 'South America'. Use the ROUND function to show the values to two decimal places."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"ROUND(population/1000000,2)":row[0],"ROUND(gdp/1000000000, 2)":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==10:
            if connection.is_connected():
                basics1 = """SELECT name, ROUND(gdp/population, -3)
    FROM world
    WHERE gdp > 1000000000000
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and per-capita GDP for those countries with a GDP of at least one trillion (1000000000000; that is 12 zeros). Round this value to the nearest 1000."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"ROUND(gdp/population, -3)":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==11:
            if connection.is_connected():
                basics1 = """SELECT name, capital
    FROM world
    WHERE LENGTH(name)=LENGTH(capital)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and capital where the name and the capital have the same number of characters."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"capital":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==12:
            if connection.is_connected():
                basics1 = """SELECT name,  capital
    FROM world
    WHERE LEFT(name,1) = LEFT(capital,1) and name<>capital
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"capital":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==13:
            if connection.is_connected():
                basics1 = """SELECT name FROM world
    WHERE name LIKE '%a%' AND 
    name  LIKE '%e%' AND 
    name  LIKE '%i%' AND 
    name  LIKE '%o%' AND 
    name  LIKE '%u%' AND 
    name NOT LIKE '% %'

    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Find the country that has all the vowels and no spaces in its name."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
            
    @app.get("/nobel")
    async def Allnobel():
            api1 = basics()
            api1.add("Question 1",(read_nobel(1)))
            api1.add("Question 2",(read_nobel(2)))
            api1.add("Question 3",(read_nobel(3)))
            api1.add("Question 4",(read_nobel(4)))
            api1.add("Question 5",(read_nobel(5)))
            api1.add("Question 6",(read_nobel(6)))
            api1.add("Question 7",(read_nobel(7)))
            api1.add("Question 8",(read_nobel(8)))
            api1.add("Question 9",(read_nobel(9)))
            api1.add("Question 10",(read_nobel(10)))
            api1.add("Question 11",(read_nobel(11)))
            api1.add("Question 12",(read_nobel(12)))
            api1.add("Question 13",(read_nobel(13)))
            api1.add("Question 14",(read_nobel(14)))
            return json.dumps(api1,cls=DecimalEncoder)

    @app.get("/nobel/{item_id}")
    def read_nobel(item_id: int):
        if item_id ==1:
            if connection.is_connected():
                basics1 = """SELECT yr, subject, winner
    FROM nobel
    WHERE yr = 1950"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Change the query shown so that it displays Nobel prizes for 1950."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==2:
            if connection.is_connected():
                basics1 = """SELECT winner
    FROM nobel
    WHERE yr = 1962 AND subject = 'Literature'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show who won the 1962 prize for Literature."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"winner":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==3:
            if connection.is_connected():
                basics1 = """SELECT yr, subject
    FROM nobel
    WHERE winner = 'Albert Einstein'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the year and subject that won 'Albert Einstein' his prize."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==4:
            if connection.is_connected():
                basics1 = """SELECT winner
    FROM nobel
    WHERE subject = 'Peace' AND yr >= 2000"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Give the name of the 'Peace' winners since the year 2000, including 2000."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"winner":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==5:
            if connection.is_connected():
                basics1 = """SELECT yr, subject, winner
    FROM nobel
    WHERE (yr >=1980 AND yr <=1989) AND subject = 'Literature'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==6:
            if connection.is_connected():
                basics1 = """SELECT *
    FROM nobel
    WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter', 'Barack Obama')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show all details of the presidential winners:

    Theodore Roosevelt
    Woodrow Wilson
    Jimmy Carter
    Barack Obama"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==7:
            if connection.is_connected():
                basics1 = """SELECT winner
    FROM nobel
    WHERE winner LIKE 'john%'
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the winners with first name John"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"winner":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==8:
            if connection.is_connected():
                basics1 = """SELECT *
    FROM nobel
    WHERE (subject = 'Physics' AND yr = '1980') OR (subject = 'Chemistry' AND yr = '1984')
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the year, subject, and name of Physics winners for 1980 together with the Chemistry winners for 1984."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==9:
            if connection.is_connected():
                basics1 = """SELECT *
    FROM nobel
    WHERE yr = 1980 AND subject NOT IN ('Chemistry', 'Medicine')
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the year, subject, and name of winners for 1980 excluding Chemistry and Medicine"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==10:
            if connection.is_connected():
                basics1 = """SELECT *
    FROM nobel
    WHERE (subject  = 'Medicine' AND yr < 1910) OR (subject = 'Literature' AND yr >= 2004)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show year, subject, and name of people who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==11:
            if connection.is_connected():
                basics1 = """SELECT *
    FROM nobel
    WHERE winner LIKE 'peter gr%nberg'
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Find all details of the prize won by PETER GRÜNBERG"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==12:
            if connection.is_connected():
                basics1 = """SELECT *
    FROM nobel
    WHERE winner = 'Eugene O''Neill'
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Find all details of the prize won by EUGENE O'NEILL"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"yr":row[0],"subject":row[1],"winner":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==13:
            if connection.is_connected():
                basics1 = """SELECT winner, yr, subject
    FROM nobel
    WHERE winner LIKE 'sir%'
    ORDER BY yr DESC, winner

    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"winner":row[0],"yr":row[1],"subject":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==14:
            if connection.is_connected():
                basics1 = """SELECT winner, subject
    FROM nobel
    WHERE yr=1984
    ORDER BY subject IN ('Physics','Chemistry'), subject, winner

    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the 1984 winners and subject ordered by subject and winner name; but list Chemistry and Physics last."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"winner":row[0],"subject":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)    
            
    @app.get("/within")
    async def Allnobel():
            api1 = basics()
            api1.add("Question 1",(read_within(1)))
            api1.add("Question 2",(read_within(2)))
            api1.add("Question 3",(read_within(3)))
            api1.add("Question 4",(read_within(4)))
            api1.add("Question 5",(read_within(5)))
            api1.add("Question 6",(read_within(6)))
            api1.add("Question 7",(read_within(7)))
            api1.add("Question 8",(read_within(8)))
            api1.add("Question 9",(read_within(9)))
            api1.add("Question 10",(read_within(10)))
            return json.dumps(api1,cls=DecimalEncoder)

    @app.get("/within/{item_id}")
    def read_within(item_id: int):
        if item_id ==1:
            if connection.is_connected():
                basics1 = """SELECT name
    FROM world
    WHERE population > (
    SELECT population
    FROM world
    WHERE name = 'Russia')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List each country name where the population is larger than that of 'Russia'."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==2:
            if connection.is_connected():
                basics1 = """SELECT name
    FROM world
    WHERE continent = 'Europe'
    AND gdp/population > (
    SELECT gdp/population
    FROM world
    WHERE name = 'United Kingdom')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the countries in Europe with a per capita GDP greater than 'United Kingdom'."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==3:
            if connection.is_connected():
                basics1 = """SELECT name, continent
    FROM world
    WHERE continent IN (SELECT continent FROM world WHERE name IN ('Argentina', 'Australia'))
    ORDER BY name"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"continent":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==4:
            if connection.is_connected():
                basics1 = """SELECT name, population
    FROM world
    WHERE population >
        (SELECT population FROM world WHERE name = 'Canada')
    AND population <
    (SELECT population FROM world WHERE name = 'Poland')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Which country has a population that is more than Canada but less than Poland? Show the name and the population."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"population":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==5:
            if connection.is_connected():
                basics1 = """SELECT name, CONCAT(ROUND(100*population/(SELECT population FROM world WHERE name='Germany')),'%')
    FROM world
    WHERE continent='Europe'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"CONCAT(ROUND(100*population/(SELECT population FROM world WHERE name='Germany')),'%')":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==6:
            if connection.is_connected():
                basics1 = """SELECT name
    FROM world
    WHERE gdp >= ALL(SELECT gdp FROM world WHERE gdp >=0 AND continent = 'Europe') AND continent != 'Europe'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==7:
            if connection.is_connected():
                basics1 = """SELECT continent, name, area
    FROM world x
    WHERE area >= ALL
    (SELECT area FROM world y
        WHERE y.continent=x.continent
        AND area>0)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Find the largest country (by area) in each continent, show the continent, the name and the area:"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"continent":row[0],"name":row[1],"area":row[2] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==8:
            if connection.is_connected():
                basics1 = """SELECT continent, name
    FROM world x
    WHERE name <= ALL(SELECT name FROM world y WHERE y.continent = x.continent)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List each continent and the name of the country that comes first alphabetically."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"continent":row[0],"name":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==9:
            if connection.is_connected():
                basics1 = """SELECT name, continent, population
    FROM world x
    WHERE 25000000  > ALL(SELECT population FROM world y WHERE x.continent = y.continent AND y.population > 0)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"continent":row[1],"population":row[1]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==10:
            if connection.is_connected():
                basics1 = """SELECT name, continent
    FROM world x
    WHERE population > ALL(SELECT population*3 FROM world y WHERE x.continent = y.continent AND population > 0 AND y.name != x.name)
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"name":row[0],"continent":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
            
    @app.get("/aggregate")
    async def Allnobel():
            api1 = basics()
            api1.add("Question 1",(read_sum(1)))
            api1.add("Question 2",(read_sum(2)))
            api1.add("Question 3",(read_sum(3)))
            api1.add("Question 4",(read_sum(4)))
            api1.add("Question 5",(read_sum(5)))
            api1.add("Question 6",(read_sum(6)))
            api1.add("Question 7",(read_sum(7)))
            api1.add("Question 8",(read_sum(8))) 
            return json.dumps(api1,cls=DecimalEncoder)

    @app.get("/aggregate/{item_id}")
    def read_sum(item_id: int):
        if item_id ==1:
            if connection.is_connected():
                basics1 = """SELECT SUM(population)
    FROM world"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the total population of the world."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"SUM(population)":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==2:
            if connection.is_connected():
                basics1 = """SELECT DISTINCT continent FROM world"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List all the continents - just once each."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"continent":row[0]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==3:
            if connection.is_connected():
                basics1 = """SELECT SUM(gdp) FROM world WHERE continent='Africa'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Give the total GDP of Africa"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"SUM(gdp)":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==4:
            if connection.is_connected():
                basics1 = """SELECT COUNT(*) FROM world WHERE area >= 1000000
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""How many countries have an area of at least 1000000"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"COUNT(*)":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==5:
            if connection.is_connected():
                basics1 = """SELECT SUM(population) FROM world WHERE name IN ('Estonia','Latvia','Lithuania')"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""What is the total population of ('Estonia', 'Latvia', 'Lithuania')"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"SUM(population)":row[0]  })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==6:
            if connection.is_connected():
                basics1 = """SELECT continent, COUNT(*) FROM world GROUP BY continent"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""For each continent show the continent and number of countries."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"continent":row[0],"COUNT(*)":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==7:
            if connection.is_connected():
                basics1 = """SELECT continent, COUNT(*) 
    FROM world
    WHERE population >= 10000000
    GROUP BY continent
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""For each continent show the continent and number of countries with populations of at least 10 million."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"continent":row[0],"COUNT(*)":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==8:
            if connection.is_connected():
                basics1 = """SELECT continent
    FROM world
    GROUP BY continent
    HAVING SUM(population) >= 100000000
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List the continents that have a total population of at least 100 million."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"continent":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)

        
    @app.get("/joins")
    async def Allnobel():
            api1 = basics()
            api1.add("Question 1",(read_joins(1)))
            api1.add("Question 2",(read_joins(2)))
            api1.add("Question 3",(read_joins(3)))
            api1.add("Question 4",(read_joins(4)))
            api1.add("Question 5",(read_joins(5)))
            api1.add("Question 6",(read_joins(6)))
            api1.add("Question 7",(read_joins(7)))
            api1.add("Question 8",(read_joins(8)))
            api1.add("Question 9",(read_joins(9)))
            api1.add("Question 10",(read_joins(10)))
            api1.add("Question 11",(read_joins(11)))
            api1.add("Question 12",(read_joins(12)))
            api1.add("Question 13",(read_joins(13))) 
            return json.dumps(api1,cls=DecimalEncoder)

    @app.get("/joins/{item_id}")
    def read_joins(item_id: int):
        if item_id ==1:
            if connection.is_connected():
                basics1 = """SELECT matchid, player 
    FROM goal
    WHERE teamid LIKE 'GER'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Modify it to show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"matchid":row[0],"player":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==2:
            if connection.is_connected():
                basics1 = """SELECT id,stadium,team1,team2
    FROM game
    WHERE id=1012"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show id, stadium, team1, team2 for just game 1012"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"id":row[0],"stadium":row[1],"team1":row[2],"team2":row[3] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==3:
            if connection.is_connected():
                basics1 = """SELECT player,teamid,stadium,mdate
    FROM game JOIN goal ON (id=matchid)
    WHERE teamid='GER'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Modify it to show the player, teamid, stadium and mdate for every German goal."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"player":row[0],"teamid":row[1],"stadium":row[2],"mdate":row[3] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==4:
            if connection.is_connected():
                basics1 = """SELECT team1, team2, player
    FROM game JOIN goal ON (id=matchid)
    WHERE player LIKE 'Mario%'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the team1, team2 and player for every goal scored by a player called Mario player LIKE 'Mario%'"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"team1":row[0],"team2":row[1],"player":row[2]  })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==5:
            if connection.is_connected():
                basics1 = """SELECT player, teamid, coach, gtime
    FROM goal JOIN eteam ON (teamid=id)
    WHERE gtime<=10"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show player, teamid, coach, gtime for all goals scored in the first 10 minutes gtime<=10"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"player":row[0],"teamid":row[1],"coach":row[2],"gtime":row[3] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==6:
            if connection.is_connected():
                basics1 = """SELECT mdate,teamname
    FROM game JOIN eteam ON (team1=eteam.id)
    WHERE coach='Fernando Santos'"""
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"mdate":row[0],"teamname":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==7:
            if connection.is_connected():
                basics1 = """SELECT player
    FROM goal JOIN game ON (id=matchid)
    WHERE stadium = 'National Stadium, Warsaw'
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'"""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"player":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==8:
            if connection.is_connected():
                basics1 = """SELECT DISTINCT player
    FROM game JOIN goal ON matchid = id 
    WHERE (team1 = 'GER' OR team2 = 'GER')
    AND teamid!='GER'
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Instead show the name of all players who scored a goal against Germany."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"player":row[0] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==9:
            if connection.is_connected():
                basics1 = """SELECT teamname,COUNT(teamid)
    FROM eteam JOIN goal ON id=teamid
    GROUP BY teamname
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show teamname and the total number of goals scored."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"teamname":row[0],"COUNT(teamid)":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==10:
            if connection.is_connected():
                basics1 = """SELECT stadium,COUNT(1)
    FROM goal JOIN game ON id=matchid
    GROUP BY stadium
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Show the stadium and the number of goals scored in each stadium."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"stadium":row[0],"COUNT(1)":row[1] })
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==11:
            if connection.is_connected():
                basics1 = """SELECT matchid,mdate,COUNT(teamid)
    FROM game JOIN goal ON matchid = id 
    WHERE (team1 = 'POL' OR team2 = 'POL')
    GROUP BY matchid,mdate
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""For every match involving 'POL', show the matchid, date and the number of goals scored."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"matchid":row[0],"mdate":row[1],"COUNT(teamid)":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==12:
            if connection.is_connected():
                basics1 = """SELECT matchid,mdate,COUNT(teamid)
    FROM game JOIN goal ON matchid = id 
    WHERE (teamid='GER')
    GROUP BY matchid,mdate
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'
    """))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"matchid":row[0],"mdate":row[1],"COUNT(teamid)":row[2]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
        elif item_id ==13:
            if connection.is_connected():
                basics1 = """SELECT mdate,team1, SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) score1, team2,  SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) score2
    FROM game LEFT JOIN goal ON matchid = id 
    GROUP BY mdate,matchid,team1,team2
    """
                cursor = connection.cursor()
                cursor.execute(basics1)
                record = cursor.fetchall()
                api1 = basics()
                api1.add("question",("""Notice in the query given every goal is listed. If it was a team1 goal then a 1 appears in score1, otherwise there is a 0. You could SUM this column to get a count of the goals scored by team1. Sort your result by mdate, matchid, team1 and team2."""))
                api1.add("sql",(basics1))
                ids = []
                for row in record:
                    ids.append({"mdate":row[0],"team1":row[1],"SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) score1":row[2],"team2":row[3],"SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) score2":row[4]})
                api1.add("Results",(ids))
                return json.dumps(api1,cls=DecimalEncoder)
            
    @app.get("/all")
    def get_all_urls():
        url_list = [{"path": route.path, "name": route.name} for route in app.routes]
        return url_list       
        
except Error as e:
            print("Error while connecting to MySQL", e)   

class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

class basics(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value
 
    
