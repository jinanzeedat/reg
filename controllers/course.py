
@auth.requires_login()
def addcourses():
    # search and add course and test if the adding course doesnot crashing in the time
    fields = [db.courses.id, db.courses.name, db.courses.instructor]
    grid = SQLFORM.grid(db.courses, csv=False, deletable=False, editable=False, create=False, searchable=fields)
    return dict(grid=grid)


@auth.requires_login()
def addcoursesbyuser():
    form = SQLFORM(db.courses)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def mycourses():
    #search
    query = (db.studentsreg.studentID == auth.user_id) & (db.studentsreg.courseID == db.courses.id) &(db.studentsreg.studentID == db.students.id) 
    fields=[db.courses.id,db.courses.name, db.courses.capacity,db.courses.instructor,db.courses.description]
    grid = SQLFORM.grid(query,fields=fields,csv=False,editable=False, create=False,searchable=fields)
    return dict(grid=grid)


def courses():
    links = [lambda row: A('Add', _href=URL('add_course', vars=dict(course_id=row.id)))]
    grid = SQLFORM.grid(db.courses, links=links, create=False, editable=False, deletable=False,csv=False,details=False)
    return dict(grid=grid)

def add_course():
    course_id = request.vars.id
    student_id = auth.user.id
    db.studentsreg.insert(studentID=student_id, courseID=course_id)
    redirect(URL('courses'))
    response.flash = 'Course added to schedule!'

def courses():
    query = ((db.courses.prerequisties == None) & (~db.courses.code.belongs(db(db.studentsreg.studentID == auth.user.id).select(db.studentsreg.courseID)))) | \
            ((db.courses.prerequisties != None) & (db.courses.prerequisties.belongs(db(db.studentsreg.status == 'Pass').select(db.studentsreg.courseID)))) & \
            (~db.courses.id.belongs(db(db.studentsreg.studentID == auth.user.id).select(db.studentsreg.courseID, join=db.courses.on(db.courses.prerequisties == db.studentsreg.courseID)))) | \
            ((db.courses.prerequisties == None) & (~db.courses.code.belongs(db(db.studentsreg.studentID == auth.user.id).select(db.studentsreg.courseID)))) | \
            ((db.courses.prerequisties.belongs(db(db.studentsreg.status == 'Pass').select(db.studentsreg.courseID))) & (~db.courses.id.belongs(db(db.studentsreg.studentID == auth.user.id).select(db.studentsreg.courseID)))) | \
            ((db.courses.prerequisties.belongs(db(db.studentsreg.status == 'Failed').select(db.studentsreg.courseID))) & (db.courses.code.belongs(db(db.studentsreg.studentID == auth.user.id).select(db.studentsreg.courseID))))

    fields = [
        db.courses.code,
        db.courses.name,
        db.courses.capacity,
        db.courses.instructor,
        db.courses.description,
        db.courseschedules.days,
        db.courseschedules.startTime,
        db.courseschedules.endTime,
        db.courseschedules.RoomNo,
    ]
    
    left = [
        db.courseschedules.on(db.courses.scheduled == db.courseschedules.id),
    ]
   
    links = [lambda row: A('Add', _href=URL('add_course', vars=dict(code=row.courses.code)))]
    grid = SQLFORM.grid(query, fields=fields, left=left, links=links, create=False, editable=False, deletable=False, csv=False, details=False)
    return dict(grid=grid)


def add_course():
    course_id = request.vars.code
    student_id = auth.user.id
    student_reg = db(db.studentsreg).select(orderby=~db.studentsreg.id).first()
    if student_reg is None:
        id = 1
    else:
        id = student_reg.id + 1
    db.studentsreg.insert(id=id, studentID=student_id, courseID=course_id)
    redirect(URL('courses'))
    response.flash = 'Course added to schedule!'