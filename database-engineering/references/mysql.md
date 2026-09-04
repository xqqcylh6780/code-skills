# MySQL Notes

Authoritative source: https://dev.mysql.com/doc/refman/en/

Verify current documentation for the deployed MySQL major version before relying on optimizer, locking, online DDL, replication, or JSON behavior.

Focus engine-specific review on:

- InnoDB transactions and locking;
- indexes and leftmost-prefix behavior;
- `EXPLAIN` and optimizer estimates;
- character set/collation semantics;
- foreign-key behavior;
- online/in-place DDL capabilities and limitations;
- binary log / replication impact for large changes;
- backup and restore procedure actually used by the project.

Do not assume PostgreSQL-specific index, constraint, or DDL behavior maps directly to MySQL.
