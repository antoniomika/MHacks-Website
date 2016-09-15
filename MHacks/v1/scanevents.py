from MHacks.models import ScanEvent as ScanEventModel
from MHacks.v1.serializers import ScanEventSerializer

# TODO: probably want to make a special ListCreateModel and UpdateDestroyModel
# for ScanEvents since they require additional permissions
from MHacks.v1.util import GenericListCreateModel, GenericUpdateDestroyModel


class ScanEvents(GenericListCreateModel):
    """A ScanEvent is an object that represents a QR code scan for a person at 
    any event at MHacks (registration, talks, lunch, etc.)
    """

    serializer_class = ScanEventSerializer
    query_set = ScanEventModel.objects.none()

    def get_queryset(self):
        date_last_updated = super(ScanEvents, self).get_queryset()

        if date_last_updated:
            query_set = ScanEventModel.objects.all().filter(last_updated__gte=date_last_updated)
        else:
            query_set = ScanEventModel.objects.all().filter(deleted=False)

        # TODO add and define this permission
        if not self.request.user.has_perm("mhacks.scanevent_admin"):
            return query_set.filter(approved=True)

        return query_set


class ScanEvent(GenericUpdateDestroyModel):
    serializer_class = ScanEventSerializer
    query_set = ScanEventModel.objects.all()
