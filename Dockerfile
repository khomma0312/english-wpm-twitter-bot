FROM python:3

RUN apt-get update
RUN apt-get -y install locales \
	vim \
	less \
	apt-utils \
    gcc \
    build-essential \
    && pip install --no-cache-dir \
    autopep8 \
    flake8 \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get install -y vim less

# youtube-dlでffmpegが必要なのでインストール
RUN apt-get install software-properties-common -y \
&& add-apt-repository ppa:mc3man/trusty-media \
&& apt-get install ffmpeg -y

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /src
COPY requirements.txt /src
COPY speech-to-text-api.json /apis/
WORKDIR /src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt