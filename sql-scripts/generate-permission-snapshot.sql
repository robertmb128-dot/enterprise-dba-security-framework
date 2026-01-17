-- Read-only permission snapshot
SELECT
    @@SERVERNAME AS server_name,
    DB_NAME() AS database_name,
    dp.name AS principal,
    perm.permission_name,
    perm.state_desc,
    SYSDATETIMEOFFSET() AS collected_at
FROM sys.database_permissions perm
JOIN sys.database_principals dp
    ON perm.grantee_principal_id = dp.principal_id;
