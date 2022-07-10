# from doro.forms import ContactForm
# from users.models import Contact
#
#
# def contact_saved(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#
#             obj = Contact()
#             obj.first_name = form.cleaned_data['place']
#             obj.last_name = form.cleaned_data['place']
#             obj.e_mail = form.cleaned_data['place']
#             obj.message = form.cleaned_data['place']
#             obj.place = form.cleaned_data['place']
#
#             obj.save()
#             return HttpResponseRedirect('/')
#         else:
#             ...
#
