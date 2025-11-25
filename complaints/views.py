from django.shortcuts import render
from .models import Complaint

# Homepage view
def home(request):
    # This will render your homepage template
    return render(request, 'complaints/home.html')


# Submit complaint view
def submit_complaint(request):
    message = None
    status = None

    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')

        if category and description:
            # Save the complaint to the database
            Complaint.objects.create(category=category, description=description)
            message = "Complaint submitted successfully!"
            status = "success"
        else:
            message = "Please fill out all fields."
            status = "error"

    return render(request, 'complaints/complaint_form.html', {"message": message, "status": status})

