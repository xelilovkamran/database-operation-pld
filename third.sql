SELECT location_id, street_address, city, state_province, country_name 
FROM locations
inner join countries on locations.COUNTRY_ID=countries.COUNTRY_ID;