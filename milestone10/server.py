from http.client import BAD_REQUEST
import report
from flask import Flask, abort, request


app = Flask(__name__)


@app.get("/birthdays")
def birthdays():

    request_month = request.args.get('month', None)
    if request_month is None:
        abort(BAD_REQUEST)

    request_department = request.args.get('department', None)
    if request_department is None:
        abort(BAD_REQUEST)

    try:
        response = report.get_BD_report(request_month, request_department)
    except:
        abort(500)
        
    return response


@app.get("/anniversaries")
def anniversaries():

    request_month = request.args.get('month', None)
    if request_month is None:
        abort(BAD_REQUEST)

    request_department = request.args.get('department', None)
    if request_department is None:
        abort(BAD_REQUEST)

    try:
        response = report.get_annivers_report(request_month, request_department)
    except:
        abort(500)

    return response


if __name__ == '__main__':
    app.run(debug=True)