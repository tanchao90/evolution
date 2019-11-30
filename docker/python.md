# Docker Python
- [python](https://hub.docker.com/_/python/)

## 示例
#### 制作自己的镜像
```
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]
```

### test
#### test2