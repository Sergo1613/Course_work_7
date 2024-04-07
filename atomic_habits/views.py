from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from atomic_habits.models import Habit
from atomic_habits.paginators import HabitPaginator
from atomic_habits.permissions import IsOwner
from atomic_habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Контроллер для создания привычки
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка привычек
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPaginator

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.filter(owner=user)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Контроллер для вывода привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Контроллер для изменения привычки
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Контроллер для удаления привычки
    """
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListAPIView(generics.ListAPIView):
    """
    Контроллер для вывода списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator
