# Docker MySQL
- [mysql/mysql-server](https://hub.docker.com/r/mysql/mysql-server/) MySQL 官方
- [mysql](https://hub.docker.com/_/mysql/) Docker 官方

## 部署
#### Docker 命令部署
- `$ docker pull mysql/mysql-server:latest`
- `$ docker run --name=mysql-docker -d mysql/mysql-server:latest`
- `$ docker ps`
- `$ docker logs mysql-docker` 输出所有日志
- `$ docker logs mysql-docker 2>&1 | grep GENERATED` 输出随机生成的密码
- `$ docker exec -it mysql-docker mysql -u root -p` 进入 docker 实例，并连接数据库，需要输入上面查到的密码
- `$ docker exec -it mysql-docker bash` 进入 docker 实例

连接数据库之后，需要重置默认密码才能继续操作：
- `mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';`

#### Docker Compose 部署
配置文件 `docker-compose.yml`

```
version: '3'
services:
  mysql-docker:
    container_name: mysql-docker
    image: mysql/mysql-server:latest
    ports:
      - 3306:3306
    volumes:
     - /home/ubuntu/data/mysql_data:/var/lib/mysql
     - /home/ubuntu/data/mysql_cnf/my.cnf:/etc/my.cnf
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: init_password
```

## 注意点
- 修改 MySQL 配置文件 `my.cnf`，修改默认字符集，具体参考 [MySQL Config](/database/mysql/config.md)