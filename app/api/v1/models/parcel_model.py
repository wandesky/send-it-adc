class Parcel(object):
    parcels = []

    def __init__(self, placedBy, weight, weightmetric, sentOn, deliveredOn, status, parcel_from, parcel_to, currentlocation):
        self.parcel_id = len(Parcel.parcels)
        self.placedBy = placedBy
        self.weight = weight
        self.weightmetric = weightmetric
        self.sentOn = sentOn
        self.deliveredOn = deliveredOn
        self.status = status
        self.parcel_from = parcel_from
        self.parcel_to = parcel_to
        self.currentlocation = currentlocation


    def get_all_parcels(self = None):
        return Parcel.parcels

    def post_parcel(self):
        Parcel.parcels.append(
            {
                "id": len(Parcel.parcels),
                "placedBy": self.placedBy,
                "weight": self.weight,
                "weightmetric": self.weightmetric,
                "sentOn": self.sentOn,
                "deliveredOn": self.deliveredOn,
                "status": self.status,
                "parcel_from": self.parcel_from,
                "parcel_to": self.parcel_to,
                "currentlocation": self.currentlocation

            }
        )
        return "success"