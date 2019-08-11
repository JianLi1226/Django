import json
from database.models import C
from django.shortcuts import render

# def sec_course(request):
#     c = Courses.objects.get(courses_name='安全')
#     courses_sec = {'方向': c.courses_name,
#                    '摘要': c.courses_summary,
#                    '授课老师': c.courses_teacher,
#                    '授课方式': c.courses_method,
#                    '课程特色': c.courses_characteristic,
#                    '试验环境': c.courses_provide_lab,
#                    '具体课程': json.loads(c.courses_detail)}
#
#     return  render(request, 'course.html')
#
# def dc_course(request)
#
# c = Courses.objects.get(courses_name='数据中心')
# courses_dc = {'方向': c.courses_name,
#               '摘要': c.courses_summary,
#               '授课老师': c.courses_teacher,
#               '授课方式': c.courses_method,
#               '课程特色': c.courses_characteristic,
#               '试验环境': c.courses_provide_lab,
#               '具体课程': json.loads(c.courses_detail)}
