FROM python:3.6.9

ADD welcome-bot.py /

RUN pip install discord.py==0.16.12

CMD [ "python", "./welcome-bot.py" ]