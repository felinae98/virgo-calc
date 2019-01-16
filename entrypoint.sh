set -ex
if [ ! -z "$SECRET_KEY" ]; then
    SECRET_KEY=$(< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};)
    echo "generate secret key"
done

exec gunicorn "app:app" \
    --bind "0.0.0.0:5000" \
    --workers 4 \
    --worker-class "gevent" \
