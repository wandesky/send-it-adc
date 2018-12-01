class Parcel(object):
    parcels = []

    def __init__(self, placedBy, weight):
        self.parcel_id = len(Parcel.parcels)
        self.placedBy = placedBy
        self.weight = weight


    def get_all_parcels(self = None):
        return Parcel.parcels

    def post_parcel(self):
        Parcel.parcels.append(
            {
                "id": len(Parcel.parcels),
                "placedBy": self.placedBy,
                "weight": self.weight
            }
        )
        return "success"