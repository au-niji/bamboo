ARG PythonVersion
FROM python:$PythonVersion

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
# install module の list を用いた pip による module の download
RUN pip install -r /tmp/requirements.txt
COPY . /var/application
# HOMEディレクトリを編集
WORKDIR /var/application/
