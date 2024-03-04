from report import report
from flask import Flask, request


app = Flask(__name__)

@app.get("/birthdays")
def birthdays():
    request_month = request.args.get('month', '')
    request_department = request.args.get('department', '')

    response = report.get_BD_report(request_month, request_department)

    return response


@app.get("/anniversaries")
def anniversaries():
    request_month = request.args.get('month', '')
    request_department = request.args.get('department', '')

    response = report.get_annivers_report(request_month, request_department)

    return response


if __name__ == '__main__':
    app.run(debug=True)