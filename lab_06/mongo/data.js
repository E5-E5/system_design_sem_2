db = db.getSiblingDB("hotel_booking");

db.hotels.insertMany([

  {
    name: "Hilton",
    city: "Amsterdam",
    address: "Center 1",
    description: "Luxury hotel",
    rating: 4.8,
    tags: ["wifi", "spa"]
  },

  {
    name: "Ibis",
    city: "Paris",
    address: "Street 2",
    description: "Cheap hotel",
    rating: 3.9,
    tags: ["parking"]
  }

])