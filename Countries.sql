Select * countries
Where languages = 'Slovene'
Group By desc language percentage

SELECT countries.name, languages.language, languages.percentage 
FROM countries
LEFT JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;
Select  countries.cities

Select countries.name Count(cities.id) As cities_num
From countries
Join cities On countries.id = cities.country_id
Group by cities_num DESC

Select countries.name, cities.population, cities.name
From countries
Left Join cities On countries.id = cities.country_id
Where country.id = 'Mexico' And cities.population > 500000
Order by cities.population DESC

Select countries.name, languages.language, language.percentage
From countries
Left Join languages On countries.id = languages.country_id
Where languages.percentage > 89
Order by languages.percentage DESC


Select countries.name, countries.surface_area, countries.population
From countries
Where countries.surface_Area > 501 And countries.population < 100,000


Select countries.government_form, countries.capital, countries.life_expectancy 
From countries
Where government_form = Constitutional_Monarchy And life_expectancy > 75 And capitol > 200

Select countries.name, cities.district, countries.name, cities.population
From countries
LEFT JOIN cities ON countries.id = cities.country_id
Where country.name = 'Argentina'
And cities.district = 'Buenos Ares'
And cities.population > 500,000

Select countries.region, Count(countries.id) as countryNumber
From countries
Group by countries.region
Order by countryNumber DESC
