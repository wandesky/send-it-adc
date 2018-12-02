class Parcel(object):
    parcels = [
        {
            # Dummy parcel data
            "parcel_id": 0,
            "placedBy": "wafula",
            "weight": "2kg",
            "weightmetric": "dummyweightmetric",
            "sentOn": "dummysentOn",
            "deliveredOn": "dummydeliveredOn",
            "status": "dummystatus",
            "parcel_from": "dummyparcel_from",
            "parcel_to": "dummyparcel_to",
            "currentlocation": "dummycurrentlocation"
        }
    ]

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

    def get_specific_parcel(self = None, parcel_id = None):
        return Parcel.parcels[parcel_id]

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
