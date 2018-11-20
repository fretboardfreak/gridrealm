FROM nginx:stable

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

# include static files
COPY dist/gridrealm/static /usr/share/nginx/html
# include client pages
# include error pages
VOLUME /usr/share/nginx/html

RUN mkdir /socket
VOLUME /socket

EXPOSE 80
