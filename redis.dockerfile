FROM redis:4.0.11

ENV REDIS_PASSWORD YOUR_PASSWORD

CMD ["sh", "-c", "exec redis-server --requirepass \"$REDIS_PASSWORD\""]
