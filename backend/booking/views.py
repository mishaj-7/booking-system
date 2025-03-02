from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Appointment
from datetime import datetime, timedelta


def get_time_slots():
    slots = []
    start = datetime.strptime("10:00", "%H:%M")
    end = datetime.strptime("17:00", "%H:%M")
    break_start = datetime.strptime("13:00", "%H:%M")
    break_end = datetime.strptime("14:00", "%H:%M")
    
    current = start
    while current < end:
        if not (break_start <= current < break_end):
            slots.append(current.strftime("%H:%M"))
        current += timedelta(minutes=30)
    return slots

@api_view(['GET'])
def available_slots(request, date):
    if request.method == 'OPTIONS':
        response = Response()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        booked_slots = Appointment.objects.filter(date=date_obj).values_list('time', flat=True)
        all_slots = get_time_slots()
        available = [slot for slot in all_slots if slot not in booked_slots]
        response = Response({'slots': available})
        response['Access-Control-Allow-Origin'] = '*'
        return response
    except ValueError:
        response = Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)
        response['Access-Control-Allow-Origin'] = '*'
        return response

@api_view(['POST'])
def book_appointment(request):
    data = request.data
    required_fields = ['name', 'phone', 'date', 'time']
    
    if not all(field in data for field in required_fields):
        response = Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        response['Access-Control-Allow-Origin'] = '*'
        return response
    
    try:
        date_obj = datetime.strptime(data['date'], '%Y-%m-%d')
        if data['time'] not in get_time_slots():
            response = Response({'error': 'Invalid time slot'}, status=status.HTTP_400_BAD_REQUEST)
            response['Access-Control-Allow-Origin'] = '*'
            return response
        
        if Appointment.objects.filter(date=date_obj, time=data['time']).exists():
            response = Response({'error': 'Slot already booked'}, status=status.HTTP_400_BAD_REQUEST)
            response['Access-Control-Allow-Origin'] = '*'
            return response
        
        Appointment.objects.create(
            date=date_obj,
            time=data['time'],
            name=data['name'],
            phone=data['phone']
        )
        response = Response({'message': 'Appointment booked successfully'})
        response['Access-Control-Allow-Origin'] = '*'
        return response
    except ValueError:
        response = Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)
        response['Access-Control-Allow-Origin'] = '*'
        return response