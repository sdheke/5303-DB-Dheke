
Description

Created a local database of the movie data using the files located at the following address: https://datasets.imdbws.com/.

Retrieved all files.

Uncompressed the files.

Processed each file into a usable format.

Re-Organized the files by filtering / combining them to fit a schema.


API

This Api will run on http://killzombieswith.us:8000/docs/.

Any data returned by a route will be paginated with a preset page size.

Movies

Find all

Filter on any field in table(year,runtime(min/max))

e.g. return all movies in 1961

e.g. return all movies with runtime > 90

e.g. return all movies with runtime between 80 and 100

Filter on actor or actress (id)

e.g. return all movies associated with a specific actress

e.g. return all movies associated with a set of actors and actresses

Filter on genre(s)

e.g return all movies in a specified genre

People

Find all

Filter on name (first or last)

Filter on movie (id)

Filter on genre(s)

Filter on "worked with id or ids"

e.g. find all actors and actresses that worked with id

Filter on profession

Genre

Find all

Profession

Find all



