from rest_framework import serializers

from atomic_habits.models import Habit
from atomic_habits.validators import (RelateAndRewardValidator, HabitRelatedHabitIsPleasantValidator,
                                      HabitPleasantValidator,
                                      CheckHabitValidator, HabitTimeDurationValidator)


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Habit """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelateAndRewardValidator(field1='related_habit', field2='reward'),
            HabitRelatedHabitIsPleasantValidator(field1='related_habit', field2='is_pleasant'),
            HabitPleasantValidator(field1='related_habit', field2='reward', field3='is_pleasant'),
            HabitTimeDurationValidator(field='duration'),
            CheckHabitValidator(field='periodicity')
        ]
