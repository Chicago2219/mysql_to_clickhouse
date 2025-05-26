
CREATE TABLE orders_raw (
  id UInt32,
  user_id UInt32,
  amount Float32,
  created_at DateTime
) ENGINE = MergeTree() ORDER BY id;

CREATE MATERIALIZED VIEW orders_by_day
ENGINE = SummingMergeTree
ORDER BY day AS
SELECT
  toDate(created_at) AS day,
  count() AS total_orders,
  sum(amount) AS total_amount
FROM orders_raw
GROUP BY day;
