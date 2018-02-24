from data_structure import acourse, astudent


st = astudent('grades.txt')
print("参加了如下专业选修课程:")
c1 = st.get_courses(cond= {"type":"专业选修"})
print(c1)
print("2016年 下学期 学分如下：")
print("\t", st.get_credits(cond={"year":"2016", "semester":"下"}))
print("2017年学分如下：")
print("\t", st.get_credits(cond={"year":"2017"}))
print("2014年专业必修 平均绩点如下：")
print("\t", st.get_gpa(cond={"year":"2014", "type":"专业必修"}))

print("总学分:", st.get_credits({}))
print("重修学分共:", st.get_credits({"study_type":"重修"}))
