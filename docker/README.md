# Docker
- [Docker](https://docker.com/) 
- [Docker Hub](https://hub.docker.com/) Docker 官方镜像仓库

## 基本概念
- 镜像（Image）
    - 特殊的文件系统，不包含动态数据
    - 分层设计，方便定制和共享
- 容器（Container）
    - 镜像的 “实例”
    - 在镜像的基础上会创建存储层，但存储数据建议使用 `数据卷（Volume）`
- 仓库（Repository）
    - 存储镜像的服务

## 学习资料
- [Docker 官方文档](https://docs.docker.com/)
- [Docker — 从入门到实践](https://github.com/yeasy/docker_practice) 通过 GitHub 维护，内容更新比较及时，适合入门和上手
- [《第一本Docker书》](https://book.douban.com/subject/26285268/) 入门书
- [《自己动手写Docker》](https://book.douban.com/subject/27082348/) 介绍实现原理 

#### Blog
- [Docker 核心技术与实现原理](https://draveness.me/docker)

#### 教程
- [和我一步步部署 kubernetes 集群](https://github.com/opsnull/follow-me-install-kubernetes-cluster)
- [Kubernetes中文社区 | 中文文档](http://docs.kubernetes.org.cn/)

## 管理工具
- [Kubernetes (K8s)](https://kubernetes.io/) 自动化容器部署、管理
- [Marathon](https://mesosphere.github.io/marathon/) 容器管理
- [DockerSlim (docker-slim)](https://github.com/docker-slim/docker-slim) Docker 镜像压缩
- [Docker Compose](https://docs.docker.com/compose/) 定义和运行多个 Docker 容器

#### Docker Machine
- [Install Docker Machine](https://docs.docker.com/machine/install-machine/)
- [Question: Permission Denied on curl and save for docker compose](https://github.com/docker/machine/issues/652)
    - `sudo chown -R $(whoami) /usr/local/bin`

## 命令（Command）
#### Docker Base Command
- `docker version`
- `docker --help`

#### Docker Container Command
- `docker run`
- `docker ps`
- `docker logs`
- `docker stop`
- `docker start`
- `docker restart`
- `docker rm`
- `docker port`
- `docker top`
- `docker inspect`
- `docker network`
- `docker exec`

#### Docker Image Command
- `docker login`
- docker login --username=<user username> --email=<user email address>
- `docker pull`
- `docker search`
- `docker push`
- `docker images`
- `docker commit`
- `docker build`
- `docker tag`
- `dokcer rmi`

#### Docker Compose Command
- `docker-compose up -d` 运行容器
- `docker-compose down`

#### 示例
- `$ docker run -it --rm ubuntu:18.04 bash`
    - `-it` 这是两个参数，一个是 -i：交互式操作，一个是 -t 终端
    - `--rm` 这个参数是说容器退出后随之将其删除
    - `ubuntu:18.04` 镜像名称
    - `bash` 镜像后面的命令，交互式 shell