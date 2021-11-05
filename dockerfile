FROM registry.cn-hangzhou.aliyuncs.com/akshare/akdocker

WORKDIR /usr/src/app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./run.py" ]
