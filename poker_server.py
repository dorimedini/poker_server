from flask import Flask, send_from_directory
import re
app = Flask(__name__)


def is_clean_path(path):
    if not re.search(r'^[a-zA-Z0-9\.,\'"\/_\-\+]+$', path):
        return False
    if re.search(r'/\.\./', path) or \
            re.search(r'^\.\./', path) or \
            re.search(r'/\.\.$', path) or \
            re.search(r'\\\.\.\\', path) or \
            re.search(r'^\.\.\\', path) or \
            re.search(r'\\\.\.$', path):
        return False
    return True


def send_from_directory_safe(directory, path):
    if not is_clean_path(path):
        return "Unsafe path requested: {}".format(path)
    return send_from_directory(directory, path)


@app.route("/js/<path>")
def get_js(path):
    return send_from_directory_safe('js', path)


@app.route("/css/<path>")
def get_css(path):
    return send_from_directory_safe('css', path)


@app.route("/html/<path>")
def get_html(path):
    return send_from_directory_safe('html', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8725)
