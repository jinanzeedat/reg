@auth.requires_login()
def addSchedule():
    form = SQLFORM(db.courseschedules)
    if form.process().accepted:
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)


@auth.requires_login()
def schedules():
    grid = SQLFORM.grid(db.courseschedules, csv=False)
    return dict(grid=grid)