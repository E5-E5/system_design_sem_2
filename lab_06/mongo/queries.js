db.hotels.insertOne({
  name: "Test Hotel",
  city: "Berlin"
})

db.hotels.find({
  city: { $eq: "Amsterdam" }
})

db.hotels.find({
  rating: { $gt: 4 }
})

db.hotels.find({
  tags: { $in: ["spa"] }
})

db.hotels.updateOne(
  { city: "Amsterdam" },
  {
    $addToSet: {
      tags: "pool"
    }
  }
)

db.hotels.deleteOne({
  name: "Test Hotel"
})

db.hotels.aggregate([
  {
    $group: {
      _id: "$city",
      average_rating: {
        $avg: "$rating"
      }
    }
  },

  {
    $sort: {
      average_rating: -1
    }
  }
])