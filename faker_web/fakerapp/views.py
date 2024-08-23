from django.shortcuts import render
from faker import Faker
from .forms import FakerForm

def generate_data(request):
    form = FakerForm()
    data = None

    if request.method == 'POST':
        form = FakerForm(request.POST)
        if form.is_valid():
            faker = Faker()
            options = form.cleaned_data['options']
            count = form.cleaned_data['count']
            data = []

            for _ in range(count):
                record = {}
                for option in options:
                    if option == 'name':
                        record['name'] = faker.name()
                    elif option == 'address':
                        record['address'] = faker.address()
                    elif option == 'email':
                        record['email'] = faker.email()
                    elif option == 'phone':
                        record['phone'] = faker.phone_number()
                    elif option == 'job_title':
                        record['job_title'] = faker.job()
                    elif option == 'company_name':
                        record['company_name'] = faker.company()
                    elif option == 'text':
                        record['text'] = faker.text()
                    elif option == 'date_of_birth':
                        record['date_of_birth'] = faker.date_of_birth()
                    elif option == 'city':
                        record['city'] = faker.city()
                    elif option == 'country':
                        record['country'] = faker.country()
                    elif option == 'credit_card_number':
                        record['credit_card_number'] = faker.credit_card_number()
                    elif option == 'ssn':
                        record['ssn'] = faker.ssn()
                    elif option == 'license_plate':
                        record['license_plate'] = faker.license_plate()
                    elif option == 'ipv4_address':
                        record['ipv4_address'] = faker.ipv4()
                    elif option == 'mac_address':
                        record['mac_address'] = faker.mac_address()
                    elif option == 'url':
                        record['url'] = faker.url()
                    elif option == 'username':
                        record['username'] = faker.user_name()
                    elif option == 'password':
                        record['password'] = faker.password()
                    elif option == 'currency':
                        record['currency'] = faker.currency()
                    elif option == 'uuid':
                        record['uuid'] = faker.uuid4()
                    # Add more fields as needed
                data.append(record)

    return render(request, 'fakerapp/generate_data.html', {'form': form, 'data': data})
