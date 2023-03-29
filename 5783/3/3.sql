SELECT name, phone, birthdate FROM customers
WHERE citystatezip = 'South Ozone Park, NY 11420' -- neighborhood of yesterday's answer
AND (
  -- intersection dates of Aries and years of the Dog
  (birthdate >= '1910-03-20' AND birthdate <= '1910-04-20') OR
  (birthdate >= '1922-03-20' AND birthdate <= '1922-04-20') OR
  (birthdate >= '1934-03-20' AND birthdate <= '1934-04-20') OR
  (birthdate >= '1946-03-20' AND birthdate <= '1946-04-20') OR
  (birthdate >= '1958-03-20' AND birthdate <= '1958-04-20') OR
  (birthdate >= '1970-03-20' AND birthdate <= '1970-04-20') OR
  (birthdate >= '1982-03-20' AND birthdate <= '1982-04-20') OR
  (birthdate >= '1994-03-20' AND birthdate <= '1994-04-20') OR
  (birthdate >= '2006-03-20' AND birthdate <= '2006-04-20') OR
  (birthdate >= '2018-03-20' AND birthdate <= '2018-04-20') OR
  (birthdate >= '2030-03-20' AND birthdate <= '2030-04-20') OR
  (birthdate >= '2042-03-20' AND birthdate <= '2042-04-20') OR
  (birthdate >= '2054-03-20' AND birthdate <= '2054-04-20') OR
  (birthdate >= '2066-03-20' AND birthdate <= '2066-04-20') OR
  (birthdate >= '2078-03-20' AND birthdate <= '2078-04-20') OR
  (birthdate >= '2090-03-20' AND birthdate <= '2090-04-20') OR
  (birthdate >= '2102-03-20' AND birthdate <= '2102-04-20')
)
