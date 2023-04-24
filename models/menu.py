# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Schedules'), False, URL('shedule', 'schedules'),[]),
    (T('Add Scehdule'), False, URL('shedule','addSchedule'),[]),
    (T('Add Course'), False, URL('course','addcourses'),[]),
    (T('My Courses'), False, URL('course','mycourses'),[]),
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

if not configuration.get('app.production'):
    _app = request.application
    response.menu += []