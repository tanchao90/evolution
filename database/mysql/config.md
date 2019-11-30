# MySQL Config

## `my.cnf`
MySQL 配置文件，可在其中增加下面内容修改字符集

```
# customized config
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
init_connect='SET NAMES utf8mb4'
init_connect='SET collation_connection = utf8mb4_unicode_ci'
character-set-client-handshake = FALSE

# character-set-client-handshake = FALSE 
# it will always use default encoding even if you will make mistake on application layer

# skip-character-set-client-handshake
# To ignore client information and use the default server character set

[client]
default-character-set = utf8mb4

[mysql]
default-character-set = utf8mb4
```
