from django.shortcuts import render
from .serializers import UserSerializer, UserPassResetMail, ProfileToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from django.core.mail import EmailMessage
from django.http import HttpResponse


def check_profile(user):
    ''' Пhоверим, существует ли связанный 1к1 объект Profile у пользователя. Если существует, вернем его, иначе создадим '''
    try:
        profile = Profile.objects.get(owner=user)
    except:
        profile = Profile(owner=user)
    return profile

def profile_tgcode_save(user):
    '''Сохраняем в Profile поле tg_code связанное с User'''
    import hashlib
    profile = check_profile(user)
    profile.tg_code = hashlib.md5(user.username.encode('utf-8') + user.password.encode('utf-8')).hexdigest()
    profile.save()

def profile_passresettoken_save(user):
    '''Генерим и сохраняем токен для ресета пароля '''
    import uuid
    profile = check_profile(user)
    profile.pass_reset_token = str(uuid.uuid4())
    profile.save()
    return profile.pass_reset_token


# Create your views here.
@api_view(['POST'])
def register(request):
    ''' Ожидается запрос формата json {'email': 'email@email.domen', 'password': 'yourpass'} '''
    logging.basicConfig(level=logging.DEBUG, filename='/home/perespimka/monyze/log.txt', format='%(asctime)s %(levelname)s %(message)s')
    logging.debug('test')
    #em = EmailMessage(subject='Test', body='Test again', to=['s.dmitrievlol@yandex.ru'])
    #em.send()
    if request.method == 'POST':

        logging.debug('test1')
        request.data['username'] = request.data['email']
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            
            logging.debug('test2')
            user = User(username=serializer.validated_data['username'], email=serializer.validated_data['email'])
            user.set_password(serializer.validated_data['password'])
            user.save()
            profile_tgcode_save(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_pass_mail(request):
    ''' Ожидается запрос формата {'email': 'email@email.domen'} '''
    serializer = UserPassResetMail(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['email']
        try:
            user = User.objects.get(username=username)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token = profile_passresettoken_save(user)
        em = EmailMessage(subject='Test', body=f'https://monyze.ru/pass_reset_dev.html?token={token}', to=['s.dmitrievlol@yandex.ru']) # не забыть сменить to
        em.send()
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def reset_pass(request):
    ''' Ожидается запрос формата {'password': 'newpass', 'token': 'token_from_email'} '''
    serializer = ProfileToken(data=request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(profile__pass_reset_token=serializer.validated_data['token'])
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.set_password(serializer.validated_data['password'])
        user.save()
        logging.debug('JOBS DONE')
        return Response(status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def test(request):
    return HttpResponse('ahahaha lol')