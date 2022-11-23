1.
  ```sql
  SELECT DISTINCT * FROM table;
  ```
2. 
  ```sql
  SELECT i FROM generate_series('2020-01-01'::DATE, '2021-01-03'::DATE, '1 day'::INTERVAL) as t(i);
  ```

3.1.
  ```sql
  SELECT id, n, d, length(cast(n AS VARCHACR))  AS k, cast(cast(n AS VARCHAR) AS INT)+1 AS s FROM task_3;
  ```

