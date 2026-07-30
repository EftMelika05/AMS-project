models:

1.user:
  1.id
  2.phonenumber
  3.username
  4.password
  5.email
  6.role(customer/provider)

2.profile:
  1.id
  2.user
  3.full-name
  4.city
  5.gender
  6.profileimage
  7.speciality
  8.bio
  9.is_verified

3.category:
  1.id
  2.name
  3.description(optional)

4.servicetype:
  1.id
  2.category(foreignkey)
  3.name
  4.description

5.providerservice
  1.id
  2.provider(foreignkey-->profile)
  3.service_type(foreignkey)
  4.title(optional)
  5.description
  6.price
  7.duration
  8.main_image

6.serviceimage:
  1.id
  2.provider_sercive(foreignkey)
  3.image
  4.description(optional)

7.workschedule:
  1.id
  2.provider(foreignkey)
  3.day_of_week
  4.start-time
  5.end_time

8.scheduleexeption
  1.id
  2.provider(foreignkey)
  3.date
  4.start_time(optional)
  5.end_time(optional)
  6.reason

9.appointment:
  1.id
  2.customer(foreignkey-->profile)
  3.provider_service(foreignkey-->provider)
  4.date
  5.start_time
  6.end_time
  7.status






