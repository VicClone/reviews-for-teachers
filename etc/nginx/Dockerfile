FROM nginx
ARG ENV
RUN rm -rf /etc/nginx/sites-enabled/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY 502.html /var/www/502.html
