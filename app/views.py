from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        form_fields = request.POST.items()
        form_list = [value for key, value in form_fields]
        master_list = [i for i in form_list[1]]
        list_form = []
        for i in range(2, len(form_list)):
            count = 0
            field_list = [j for j in form_list[i]]
            for j in field_list:
                if j in master_list:
                    master_list.remove(j)
                    count += 1
            if count == len(field_list):
                list_form.append("Yes")
            else:
                list_form.append('No')
        context = {'field1': list_form[0], 'field2': list_form[1], 'field3': list_form[2], 'field4': list_form[3]}
        return render(request, 'home.html', context=context)
    return render(request, 'home.html')
