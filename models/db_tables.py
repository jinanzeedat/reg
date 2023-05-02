import datetime

db.define_table('courses',
    Field('id','integer', required=True, notnull=True),
    Field('name','string'),
    Field('description','string'),
    Field('prerequisties','string','referance courses',requires=IS_IN_DB(db,'courses.id','%(id)s')),
    Field('instructor','string'),
    Field('capacity','integer'),
    Field('scheduled','integer',requires=IS_IN_DB(db,'courseschedules.id','%(days)s: %(startTime)s -%(endTime)s')),

)

db.define_table('courseschedules',
    Field('id','integer'),
    Field('days','string'),
    Field('startTime','time', default=datetime.time(0,0)),
    Field('endTime','time', default=datetime.time(0,0)),
    Field('RoomNo','string',requires=IS_IN_DB(db,'rooms.code','%(code)s'))
    
)

db.define_table('rooms',
Field ('code','string', required=True, notnull=True),
primarykey=['code']
)

db.define_table('students',
    Field('id','integer', required=True, notnull=True),
    Field('first_name','string'),
    Field('last_name','string'),
    Field('email','string'),
    Field('password','string'),
    Field('registration_key','string'),
    Field('reset_password_key','string'),    
    Field('registration_id','string'),
)

db.define_table('studentsreg',
    Field('id','integer', required=True, notnull=True),
    Field('studentID','integer',requires=IS_IN_DB(db,'students.id','%(id)s')),
    Field('courseID','integer',requires=IS_IN_DB(db,'courses.id','%(id)s')),
    Field('status','string'),
)