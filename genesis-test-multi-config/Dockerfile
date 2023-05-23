FROM nginx:latest

LABEL maintainer="jasontian@unity3d.com"


RUN mkdir /usr/share/nginx/html/element
COPY ./element/ /usr/share/nginx/html/element/
COPY ./docker/default.conf /etc/nginx/conf.d/default.conf
