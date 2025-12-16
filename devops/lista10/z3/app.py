from flask import Flask, request, Response
from prometheus_client import Counter, Summary, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS_COUNT = Counter(
    "app_requests_total", "Liczba żądań do aplikacji", ["method", "endpoint"]
)

EXCEPTIONS = Counter(
    "app_exceptions_total",
    "Liczba wyjątków występujących w aplikacji",
    ["endpoint", "exception_type"],
)

PRINT_NUMBER = Summary(
    "app_print_number_summary", "Podsumowanie czasu obsługi print_number"
)


@app.errorhandler(Exception)
def catch_all(e):
    EXCEPTIONS.labels(endpoint=request.path, exception_type=type(e).__name__).inc()


@app.before_request
def count_requests():
    REQUESTS_COUNT.labels(method=request.method, endpoint=request.path).inc()


@app.route("/hello")
def hello():
    return "Hello, World!"


@app.route("/print_number")
def print_number():
    num_str = request.args.get("number", None)

    if num_str is None:
        return "Brak parametru 'number'", 400

    num = float(num_str)

    PRINT_NUMBER.observe(num)

    return f"Number: {num}", 200


@app.route("/crash")
def crash():
    raise KeyError("This is a simulated crash!")


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
