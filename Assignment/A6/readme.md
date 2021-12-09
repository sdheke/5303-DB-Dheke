
Description

Api will run on port 8003 on this server http://143.244.188.178/:8003

Loaded the restaurant DataBase (restaurant.json) on my server using MongoDB.

Any Data returned by a route will be paginated with a preset page size.

Created indexes for certain queries that allow the runtime to be faster also allow certain data to be processed.

Routes:

Restaurants

All restaurants (paginated result).

Unique restaurant categories.

All restaurants in a category.

All restaurants in a list of 1 or more zip codes.

All restaurants near Point(x,y).

All restaurants with a min rating of X.
