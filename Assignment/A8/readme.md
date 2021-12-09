
Description

To compare and see the distinctions between Redis and MongoDB and Mysql.

This experiment should time each transaction and calculate the averages.

Each aggregation should be applied to a database that is configured with slight differences.

Do n searches for single values.

Do n searches for multiple values.

Do n updates to existing documents.

Do n deletes

One possible approach could be:

Set N, where N is number of items being inserted, to:
50000
100000
500000
1 Million



When searching for a single values:

MongoDB is faster with the lowest time.

Redis is the second fastest.

MySql come in last place.

![single (1)](https://user-images.githubusercontent.com/54680118/145337242-b058809b-8a16-4f75-a957-bdf4cfdedc1f.png)


When searching for multiple values:

MySql is faster when the size of N is smaller.

MongoDB is the fastest when the size of N get bigger.

Redis come in last place.


![multi](https://user-images.githubusercontent.com/54680118/145337296-9921a34c-cb39-4106-9274-12a28515d37b.png)


When Doing N update:

Redis is faster with the lowest time.

MySql is the second fastest.

MongoDB come in last place.

![update](https://user-images.githubusercontent.com/54680118/145337345-ef5f54d5-494c-4e2e-b124-6fa471d9db7a.png)


