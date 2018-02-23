def grade_to_gpa(g):
	g = float(g)
	if g < 0 or g > 100:
		raise ValueError(g, ":grade is wrong!")
	elif g>=90:
		gpa=4.
	elif g>=85:
		gpa=3.7
	elif g>=82:
		gpa=3.3
	elif g>=78:
		gpa=3.0
	elif g>=75:
		gpa=2.7
	elif g>=72:
		gpa=2.3
	elif g>=68:
		gpa=2.0
	elif g>=64:
		gpa=1.5
	elif g>=60:
		gpa=1.0
	else:
		gpa=0
	return gpa


class acourse:
	def __init__(self, content):
		c = content.strip()
		c = c.split('\t')
		attr = ['title', 'name', 'type', 'credits', 'tname', 'department',
			'study_type', 'year', 'semester', 'grade']
		for i, a in enumerate(attr):
			try:
				setattr(self, a, c[i])
			except Exception as e:
				print(e)


class astudent:
	def __init__(self, fname):
		# 从文件中提取学生course_list with relating information
		self.course_list = []

		with open(fname, mode='r') as f:
			lines = f.readlines()
			for line in lines:
				self.course_list.append(acourse(line))
	def filter_list(self, cond):
		l = []
		for i in self.course_list:
			fit_cond = True
			for k,v in cond.items():
				if not (hasattr(i, k) and getattr(i, k)==v):
					fit_cond=False
			if fit_cond:
				l.append(i)
		return l

	def get_credits(self, cond=None):
		
		l = self.filter_list(cond)
		credits = 0
		for course in l:
			if hasattr(course, 'credits'):
				credits += float(course.credits)
		return credits


	def get_courses(self, cond=None):
		l = self.filter_list(cond)
		courses = []
		for c in l:
			courses.append(c.name)
		return courses


	def get_gpa(self, cond=None):
		l = self.filter_list(cond)
		credits = 0
		total_gpa = 0
		for c in l:
			try:
				total_gpa += grade_to_gpa(c.grade) * float(c.credits)
				credits += float(c.credits)
			except Exception as e:
				print("one course was not graded. need checking...")
		return total_gpa/credits