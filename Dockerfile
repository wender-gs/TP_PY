FROM ubuntu:latest

RUN apt update && apt upgrade -y

RUN apt install wget gnupg gnupg2 gnupg1 -y

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt -y update

RUN apt install google-chrome-stable git python3 python3-pip -y

RUN git clone https://github.com/wender-gs/TP_PY.git

WORKDIR /TP_PY

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

CMD [ "python3", "app.py" ]