
    #     zero_message = "Not aloud division by 0 !!"
    #     return render_template("zero.html", zero_message=zero_message)
    # return render_template("app.html")
    #
    #
    # elif operation == "divide":
    #     try:
    #         sum = float(num1) / float(num2)
    #     except ZeroDivisionError:
    #         zero_message = "Not aloud division by 0 !!"
    #         return render_template("zero.html", zero_message=zero_message)
    #     return render_template("app.html")
    # else:
    #     return render_template("app.html", sum=sum)


#
# @app.route("/calculation", methods=["GET", "POST"])
# def send():
# if request.method == "POST":
#     num1 = request.form["num1"]
#     num2 = request.form["num2"]
#     operation = request.form["operation"]
#
#     if not num1 or not num2:
#         error_message = "All Form Fields Required.."
#         return render_template("page_not_found.html", error_message=error_message)


#
#
# # @app.route("/", methods=["POST"])
# # def sendFirst(num1):
# #     if request.method == "POST" and "num1" in request.form:
# #         num1 = request.form.get["num1"]
# #     return render_template("index.html", num1=num1)
# #
# #
# # @app.route("/", methods=["POST"])
# # def sendSecond(num2):
# #     if request.method == "POST" and "num2" in request.form:
# #         num2 = request.form.get["num2"]
# #     return render_template("index.html", num2=num2)
# #
# #
# # @app.route("/", methods=["POST", "GET"])
# # def operation():
# #     if request.method == "POST" and "operation" in request.form:
# #         operation = request.form.get["operation"]
# #         if operation == "add":
# #             sum = float("num1") + float("num2")
# #             return render_template("index.html", sum=sum)
# #         elif operation == "sub":
# #             sum = float("num1") - float("num2")
# #             return render_template("index.html", sum=sum)
# #         elif operation == "multi":
# #             sum = float("num1") * float("num2")
# #             return render_template("index.html", sum=sum)
# #         elif operation == "divide":
# #             sum = float("num1") / float("num2")
# #             return render_template("index.html", sum=sum)
# #         else:
# #             return render_template("index.htm")
# #     return render_template("index.html")
#
#
# # @app.errorhandler(404)
# # def error(error):
# #     return render_template("index.html", error=error), 404

