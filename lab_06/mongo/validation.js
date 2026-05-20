db = db.getSiblingDB("hotel_booking");

db.createCollection("hotels", {

  validator: {

    $jsonSchema: {

      bsonType: "object",

      required: [
        "name",
        "city",
        "address"
      ],

      properties: {

        name: {
          bsonType: "string"
        },

        city: {
          bsonType: "string"
        },

        address: {
          bsonType: "string"
        },

        rating: {
          bsonType: "double",
          minimum: 0,
          maximum: 5
        },

        tags: {
          bsonType: "array"
        }
      }
    }
  }
})