from rest_framework.fields import CharField, ChoiceField
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from MHacks.models import Event as EventModel, Location as LocationModel
from serializers import UnixEpochDateField, GenericListCreateModel, GenericUpdateDestroyModel, DurationInSecondsField

class ScanEventSerializer(ModelSerializer):
    # TODO
    pass

class ScanEvent(GenericListCreateModel):
    # TODO
    pass
