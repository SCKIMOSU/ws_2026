from django.http import HttpResponse
from .models import Reservation, Customer


def reservation_list(request):
    reservations = Reservation.objects.all().order_by('reserve_date')

    lines = [
        "<h1>Reservation 목록</h1>",
        "<table border='1'>",
        "<tr><th>ID</th><th>Name</th><th>예약일</th><th>방 번호</th></tr>"
    ]
    for r in reservations:
        lines.append(
            f"<tr><td>{r.id}</td><td>{r.name}</td>"
            f"<td>{r.reserve_date}</td><td>{r.room_num}</td></tr>"
        )
    lines.append("</table>")

    return HttpResponse("".join(lines))



def customer_list(request):
    customers = Customer.objects.all()

    lines = [
        "<h1>Customer 목록</h1>",
        "<table border='1'>",
        "<tr><th>ID</th><th>Name</th><th>Age</th><th>Address</th></tr>"
    ]
    for c in customers:
        lines.append(
            f"<tr><td>{c.id}</td><td>{c.name}</td>"
            f"<td>{c.age}</td><td>{c.address}</td></tr>"
        )
    lines.append("</table>")

    return HttpResponse("".join(lines))
