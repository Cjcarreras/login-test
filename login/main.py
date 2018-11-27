#!/usr/bin/env python

import os
import webapp2
import jinja2

current_path = os.path.dirname(__file__)
template_dir = os.path.join(current_path, "templates")

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape= False)


class BaseHandler(webapp2.RequestHandler):
    def render_templates(self, template_filename, params=None):
        if params is None:
            params = {}

        template = jinja_env.get_template(template_filename)
        response = template.render(params)

        return self.response.write(response)


class MainHandler(BaseHandler):
    def get(self):
        return self.render_templates("login-index.html")


class CalculatorHandler(BaseHandler):
    def get(self):
        self.render_templates("calculator.html", {})

    def post(self):
        first_num = float(self.request.get("first-number"))
        second_num = float(self.request.get("second-number"))
        operation = self.request.get("operation")
        result = None

        if operation == "+":
            result = first_num + second_num
        elif operation == "-":
            result = first_num - second_num
        elif operation == "*":
            result = first_num * second_num
        elif operation == "/":
            result = first_num / second_num

        return self.response.out.write("El resultado es: " + str(result))


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/calculator', CalculatorHandler)
], debug=True)


