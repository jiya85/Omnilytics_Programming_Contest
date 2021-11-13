from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import random
import string
from django.http.response import HttpResponse
from drf_yasg import openapi

response_schema_dict_file_generator = {
    "200": openapi.Response(
        description="Click on the Example Value text below to see sample response",
        examples={
            "application/json": {
                    "ack_timestamp": "timestamp",
                    "generated_objects": {
                        "alphabetical_string": {
                            "generated_string": "string",
                            "obj_length": "integer"
                        },
                        "real_number": {
                            "generated_number": "float",
                            "obj_length": "integer"
                        },
                        "integer": {
                            "generated_integer": "integer",
                            "obj_length": "integer"
                        },
                        "alphanumeric": {
                            "generated_alphanumeric": "string",
                            "obj_length": "integer"
                        }
                    },
                    "file_content": "string",
                    "status": {
                        "status_code": "integer",
                        "msg": "string"
                    }
                }
        }
    ),
}


class Contest:
    @staticmethod
    @csrf_exempt
    @swagger_auto_schema(method='get', operation_description="API for File Object Generation",
                         responses=response_schema_dict_file_generator)
    @api_view(['GET'], )
    def generate_file(request):
        random_alphabetical_string = ''.join(random.choices(string.ascii_letters, k=Contest.generate_random_number()))
        random_real_number = random.uniform(-Contest.generate_random_number(), Contest.generate_random_number())
        random_integer_number = random.randint(-2147483647, 2147483647)
        random_alphanumeric_string = ''.join(
            random.choices(string.ascii_letters + string.digits, k=Contest.generate_random_number()))

        with open('file_generator/generated_file/file', 'w') as f:
            f.write(random_alphabetical_string + "," + str(random_real_number) + "," + str(
                random_integer_number) + "," + random_alphanumeric_string)
        f.close()
        return Response(
            {
                "ack_timestamp": datetime.now(),
                "generated_objects":
                    {
                        "alphabetical_string": {
                            "generated_string": random_alphabetical_string,
                            "obj_length": len(random_alphabetical_string)
                        },
                        "real_number": {
                            "generated_number": random_real_number,
                            "obj_length": len(str(random_real_number))
                        },
                        "integer": {
                            "generated_integer": random_integer_number,
                            "obj_length": len(str(random_integer_number))
                        },
                        "alphanumeric": {
                            "generated_alphanumeric": random_alphanumeric_string,
                            "obj_length": len(random_alphanumeric_string)
                        },
                    },
                "file_content": random_alphabetical_string + "," + str(random_real_number) + "," + str(
                    random_integer_number) + "," + random_alphanumeric_string,
                "status":
                    {
                        "status_code": 200,
                        "msg": "File Content Generated Successfully!",
                    }
            }
        )

    @staticmethod
    def generate_random_number():
        random_number = random.randint(20, 200)
        return random_number

    @staticmethod
    @csrf_exempt
    @api_view(['GET'], )
    def download_file(request):
        try:
            path = open('file_generator/generated_file/file', 'r')
            response = HttpResponse(path, content_type='text/plain')
            response['Content-Disposition'] = "attachment; filename=%s" % 'file'
            return response
        except FileNotFoundError as e:
            return Response(
                {
                    "ack_timestamp": datetime.now(),
                    "status":
                        {
                            "status_code": 404,
                            "msg": "File not found. Please generate the file first!",
                        }
                }, status=404
            )

