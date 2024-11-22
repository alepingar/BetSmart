from django.shortcuts import render
from .models import EventoDeportivo
from django.shortcuts import render, get_object_or_404
from .models import EventoDeportivo, Apuesta


def lista_eventos(request):
    eventos = EventoDeportivo.objects.all()
    return render(request, 'sports/eventos.html', {'eventos': eventos})


def hacer_apuesta(request, evento_id):
    evento = get_object_or_404(EventoDeportivo, id=evento_id)
    if request.method == 'POST':
        monto = request.POST['monto']
        equipo = request.POST['equipo']
        nueva_apuesta = Apuesta(
            usuario="usuario_demo",  # Simulación, reemplázalo con autenticación real
            evento=evento,
            monto=monto,
            equipo_apostado=equipo,
        )
        nueva_apuesta.save()
        return render(request, 'sports/apuesta_exitosa.html', {'apuesta': nueva_apuesta})
    return render(request, 'sports/hacer_apuesta.html', {'evento': evento})
