FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
RUN mkdir AutoKrakinz
RUN apt update 
RUN apt upgrade -y 
RUN apt install git -y 
RUN apt-get install curl -y && apt install python3 -y && apt install python3-pip -y
RUN apt install -y ffmpeg opus-tools bpm-tools 
RUN curl -sL https://deb.nodesource.com/setup_17.x | bash -
RUN apt install nodejs -y
RUN cd AutoKrakinz
RUN git clone https://github.com/krakinz/Sasuke.git
RUN cd Sasuke
WORKDIR /Sasuke
RUN npm install --force
RUN pip install -r Sasuke_core/Krakinz_lab.txt
CMD python3 Sasuke_lab.py
