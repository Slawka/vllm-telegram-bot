FROM python:3.12-alpine

ARG APPHOMEDIR=code
ARG USERNAME=user
ARG USER_UID=1001
ARG USER_GID=1001
ARG PYTHONPATH_=${APPHOMEDIR}

WORKDIR /${APPHOMEDIR}

COPY requirements.txt requirements.txt
#COPY ./bot /${APPHOMEDIR}

# Configure app home directory
RUN \
    addgroup -g "$USER_GID" "$USERNAME" \
    && adduser --disabled-password -u "$USER_UID" -G "$USERNAME" -h /"$APPHOMEDIR" "$USERNAME" \
    && chown "$USERNAME:$USERNAME" -R /"$APPHOMEDIR"

RUN apk upgrade --no-cache

# Install dependency packages, upgrade pip and then install requirements
RUN \
    apk add --no-cache gcc g++ \
    && python -V \
    && python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN pip3 install --no-cache-dir python-telegram-bot openai telegramify-markdown python-dotenv==1.0.0 aiogram==3.13.1
RUN apk del --no-cache gcc g++

USER ${USERNAME}

CMD [ "python3", "-u", "run.py"]
