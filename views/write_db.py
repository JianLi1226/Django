import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Django.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')
django.setup()


from database.models import Courses
import json

sec = {
    '方向': '网络安全',
    '摘要': '主要讲解网络安全知识',
    '授课老师': '现任明教教主',
    '授课方式': '在线,网真,本地',
    '是否提供实验环境': '不提供分解试验台',
    '具体课程': '["FW","VPN","IDS","Hacker"]'
}

dc = {
    '方向': '数据中心',
    '摘要': '主要讲解数据中心知识',
    '授课老师': '在线,网真,本地',
    '授课方式': '不提供分解试验台',
    '是否提供实验环境': '提供VPN访问云试验台',
    '具体课程': '["Nexus","UCS","Storage"]'
}



course_list = [sec, dc]
# for x in course_list:
#     s = Courses(courses_name=x.get('方向'),
#                 courses_teacher=x.get('授课老师'),
#                 courses_method=x.get('授课方式'),
#                 courses_summary=x.get('摘要'),
#                 courses_provide_lab=x.get('是否提供实验环境'),
#                 courses_detail=json.dumps(x.get('具体课程'))
#                 )
#     s.save()

# Get 只能用来返回一条记录，当多条记录命中，则会报错
# try:
#     sec_info = Courses.objects.get(courses_name='网络安全')
# except Courses.DoesNotExist:
#     pass
# except Courses.MultipleObjectsReturned:
#     pass

sec_result = Courses.objects.filter(courses_name='网络安全')
Courses.objects.filter(id=2).delete()


