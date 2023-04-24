
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