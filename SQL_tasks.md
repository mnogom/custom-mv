1.
  ```sql
  SELECT DISTINCT * FROM table;
  ```
2. 
  ```sql
  SELECT i FROM generate_series('2020-01-01'::DATE, '2021-01-03'::DATE, '1 day'::INTERVAL) as t(i);
  ```

3.
  ```sql
  SELECT id, n, d, length(cast(n as VARCHACR))  as k, cast(cast(n as VARCHAR) as INT)+1 as s from task_3;
  ```

