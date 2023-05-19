def handle_uploaded_file(f):  
    with open('AdminPanel/static/logo/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
def photo_uploaded_file(f):  
    with open('AdminPanel/static/Student/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 