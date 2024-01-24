def take_user_data(r): #r being the request Object
    if r.method == "POST":
        year = str(r.form["year_"])
        matric =str(r.form["matricno_"])
        password = str(r.form["pass_"])
        department = str(r.form["dept_"])
        fname = str(r.form["fname_"])
        oname = str(r.form["oname_"])
        lname = str(r.form['lname_'])
        return (year,matric,password,department,fname,oname,lname)


        
