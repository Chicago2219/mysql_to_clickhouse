CREATE TABLE IF NOT EXISTS default.transactions (
    id UInt64,
    user_id UInt64,
    amount Float64,
    created_at DateTime
) ENGINE = MergeTree
ORDER BY id;


CREATE MATERIALIZED VIEW IF NOT EXISTS default.user_summary_mv
ENGINE = AggregatingMergeTree
ORDER BY user_id
AS
SELECT
    user_id,
    countState() AS transaction_count,
    sumState(amount) AS total_amount
FROM default.transactions
GROUP BY user_id;
