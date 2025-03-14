from django.shortcuts import render

def home(request):
    animals = [
        {
            'name': 'Лев',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg',
            'description': 'Лев — крупное хищное млекопитающее, обитающее в саваннах Африки.',
            'link': '/lion/'  # Ссылка на льве
        },
        {
            'name': 'Слон',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg',
            'description': 'Слон — самое крупное сухопутное животное, живёт в Африке и Азии.',
            'link': '/elephant/'  # Ссылка на слона
        }
    ]
    return render(request, 'home.html', {'animals': animals})

def elephant_info(request):
    return render(request, 'elephant.html')

def lion_info(request):
    return render(request, 'lion.html')
