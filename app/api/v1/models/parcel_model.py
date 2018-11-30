class Parcel(object):
    parcels = []

    def __init__(self, parcel_id = None):
        self.parcel_id = parcel_id

    def get_all_parcels(self = None):
        return Parcel.parcels