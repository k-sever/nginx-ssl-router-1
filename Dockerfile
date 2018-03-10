FROM openresty/openresty:alpine

ADD build/etc/nginx /etc/nginx/

EXPOSE 80 443 8080 8081
